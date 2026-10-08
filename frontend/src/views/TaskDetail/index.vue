<script setup lang="ts">
import { onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router'
import { getTaskDetail, type TaskDetail, rulePreview } from '@/api/task'
import { ElLoading, type LoadingInstance } from 'element-plus'
import { notify } from '@/utils/notification'
import { rulesConfig, ruleDefaultConfig } from '@/utils/const'

const route = useRoute()

interface RuleConfigs {
  format?: string
  [key: string]: any
}

interface ColumnRule {
  type: string
  configs: RuleConfigs
}

interface ColumnInfo {
  name: string
  isDate: boolean
  isTime: boolean
  rule: ColumnRule
}

let loadingInstance: LoadingInstance | undefined
const taskId: string = route.params.taskId as string
const columnData = ref<ColumnInfo[]>([])
const totalRows = ref(0)
const sampleData = ref<any[]>([])
const fileName = ref<string>('')
const previewData = ref<object[]>([])
const ruleMap = ref<Record<string, any>>({})

const setLoading = (loading: boolean) => {
  if (loading) {
    // 防止重复创建
    if (!loadingInstance) {
      loadingInstance = ElLoading.service({
        lock: true,
        text: '任务分析中',
        background: 'rgba(0, 0, 0, 0.7)',
      })
    }
  } else {
    loadingInstance?.close()
    loadingInstance = undefined
  }
}

onMounted(async () => {
  try {
    let result = await getTaskDetail(taskId)

    while (result.status !== 'ready') {
      setLoading(true)
      await new Promise(resolve => setTimeout(resolve, 1000))

      result = await getTaskDetail(taskId)
    }

    handleResult(result)

  } catch (error) {
    notify('接口调用失败', 'error')
  } finally {
    setLoading(false)
  }
})

const handleResult = (result: TaskDetail) => {
  totalRows.value = result.rows ?? 0
  sampleData.value = result.sample_data ?? []
  fileName.value = result.filename ?? ''
  for (const columnName of result.columns ?? []) {
    let currentRule = result.rules?.[columnName]
    columnData.value.push({
      name: columnName,
      isDate: result.date_columns?.includes(columnName) ?? false,
      isTime: result.time_columns?.includes(columnName) ?? false,
      rule: Object.keys(currentRule).length > 0 ? {type: currentRule.rule_type, configs: currentRule} : {type: "none", configs: {}}
    })
    ruleMap.value[columnName] = {}
    if (Object.keys(currentRule).length !== 0) {
      let ruleType = currentRule.rule_type
      ruleMap.value[columnName][ruleType] = currentRule
    }
  }
}

const getNestedValue = (obj: Record<string, any>, path: string) => {
  return path.split('.').reduce((current, key) => {
    return current?.[key]
  }, obj)
}

const setNestedValue = (
  obj: Record<string, any>,
  path: string,
  value: any
) => {
  const keys = path.split('.')
  const lastKey = keys.pop()!

  let current = obj

  for (const key of keys) {
    if (!current[key] || typeof current[key] !== 'object') {
      current[key] = {}
    }

    current = current[key]
  }

  current[lastKey] = value
}

const getConfigModel = (
  configs: Record<string, any>,
  key: string
) => {
  return computed({
    get: () => getNestedValue(configs, key),
    set: (value) => setNestedValue(configs, key, value)
  })
}

const getPreivew = async () => {
  let rules: Record<string, object> = {}
  for (let columnInfo of columnData.value) {
    rules[columnInfo.name] = columnInfo.rule.configs
  }
  const result = await rulePreview(taskId, {"rules": rules})
  previewData.value = result
}

const getColumnCurrentRule = (columnName: string) => {
  for (let columnInfo of columnData.value) {
    if (columnInfo.name === columnName) {
      return columnInfo.rule.configs
    }
  }
  return {}
}

const setColumnRule = (columnName: string, ruleType: string, extra: object) => {
  for (let [index, columnInfo] of columnData.value.entries()) {
    if (columnInfo.name === columnName) {
      if (ruleType in ruleMap.value[columnName]) {
        columnData.value[index].rule.configs = {...ruleMap.value[columnName][ruleType], ...extra}
      } else {
        columnData.value[index].rule.configs = {...ruleDefaultConfig[ruleType], ...extra}
      }
    }
  }
}

const checkColumnRuleType = (columnName: string, value: any) => {
  const curConfig = getColumnCurrentRule(columnName)
  let format = null
  if (Object.keys(curConfig).length !== 0) {
    let ruleType = curConfig.rule_type
    ruleMap.value[columnName][ruleType] = curConfig
    if ('format' in curConfig) {
      format = curConfig['format']
    }
  }
  setColumnRule(columnName, value, format != null ? {format} : {})
}

const cancelPreview = () => {
  previewData.value = []
}

const runTask = async () => {}
</script>

<template>
  <div class="main" v-if="fileName != ''">
    <el-row class="main-title">
      <el-col :span="16">
        <el-row>
          <div class="file-info">
            {{ fileName }} - {{ totalRows }} rows
          </div>
        </el-row>
      </el-col>
      <el-col :span="8">
        <el-row justify="end">
          <el-button type="primary" round @click="getPreivew">预览</el-button>
          <el-button type="primary" round @click="runTask">运行</el-button>
        </el-row>
      </el-col>
    </el-row>
    <el-divider class="divider" />
    <!-- 字段规则配置 -->
    <template v-for="(columnInfo, index) in columnData" :key="index">
      <el-row justify="start" class="column-name">
        字段名：{{ columnInfo.name }}
      </el-row>
      <el-row class="form-row">
        <div>
          <p>脱敏规则</p>
          <el-select v-model="columnInfo.rule.type" class="rule-select" @change="checkColumnRuleType(columnInfo.name, $event)">
            <template v-for="(item, key) in rulesConfig" :key="key">
              <el-option
                v-if="(!item.isDate || (item.isDate && columnInfo.isDate)) && (!item.isTime || (item.isTime && columnInfo.isTime))"
                :key="key"
                :label="item.label"
                :value="key"
              />
            </template>
          </el-select>
        </div>
        <template v-for="ruleConfig in rulesConfig[columnInfo.rule.type].fields" :key="ruleConfig.key">
          <div>
            <p>{{ ruleConfig.label }}</p>
            <el-input
              v-if="ruleConfig.type === 'input'"
              :disabled="ruleConfig.disabled"
              v-model="getConfigModel(columnInfo.rule.configs, ruleConfig.key).value"
            />
            <el-input-number
              v-if="ruleConfig.type === 'number'"
              :min="!ruleConfig.allowNegative ? 1 : undefined"
              v-model="getConfigModel(columnInfo.rule.configs, ruleConfig.key).value"
            />
            <el-select
              v-if="ruleConfig.type === 'select'"
              v-model="getConfigModel(columnInfo.rule.configs, ruleConfig.key).value"
              class="field-select"
              :filterable="true"
            >
              <el-option
                v-for="(optionItem, oIndex) in ruleConfig.options"
                :key="oIndex"
                :label="optionItem.label"
                :value="optionItem.value"
              />
            </el-select>
            <el-select
              v-if="ruleConfig.type === 'datetimeSelect'"
              v-model="getConfigModel(columnInfo.rule.configs, ruleConfig.key).value"
              class="field-select"
              :filterable="true"
              multiple
              collapse-tags
            >
              <template v-for="optionItem in ruleConfig.options" :key="optionItem.value">
                <el-option
                  v-if="columnInfo.rule.configs.format?.includes(optionItem.value)"
                  :label="optionItem.label"
                  :value="optionItem.value"
                />
              </template>
            </el-select>
          </div>
        </template>
      </el-row>
      <el-divider v-if="index != columnData.length - 1" class="divider" border-style="dashed" />
    </template>
    <el-divider class="divider" />
    <!-- 样本数据 -->
    <el-row class="preview-title">
      <el-col :span="12">
        <el-row>预览数据</el-row>
      </el-col>
      <el-col :span="12">
        <el-row justify="end">
          <el-button :disabled="previewData.length === 0" round @click="cancelPreview">复原</el-button>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-table :data="previewData.length > 0 ? previewData : sampleData" height="500" border>
        <el-table-column
          v-for="column in columnData"
          :key="column.name"
          :prop="column.name"
          :label="column.name"
        />
      </el-table>
    </el-row>
  </div>
</template>

<style scoped>
  .main-title {
    display: flex;
    align-items: center;
  }
  .file-info {
    font-size: 24px;
    font-weight: bolder;
  }
  .form-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;

    .column-name {
      font-size: 16px;
      font-weight: bold;
    }

    p {
      font-size: 14px;
      text-align: left;
    }

    .rule-select, .field-select {
      width: 180px;
    }
  }
  .divider {
    margin: 10px 0;
  }
  .preview-title {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }
</style>
