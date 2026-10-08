<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import type { UploadFile, UploadUserFile, ComponentSize } from 'element-plus'
import { uploadFile, getTaskList, type TaskInfo } from '@/api/task'
import { notify } from '@/utils/notification'
import router from '@/router'

const fileList = ref<UploadUserFile[]>([])
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)
const tableData = ref<TaskInfo[]>([])
const size = ref<ComponentSize>('default')
const background = ref(false)
const disabled = ref(false)

const handleFileChange = async (file: UploadFile) => {
  if (!file.raw) {
    return
  }
  try {
    const result = await uploadFile(file.raw)
    notify('上传成功', 'success')
    let taskId = result.task_id
    router.push(`/task/${taskId}`)
  } catch (error) {
    notify('上传失败', 'error')
  }
}

const getList = async () => {
  try {
    const result = await getTaskList({page: currentPage.value, page_size: pageSize.value})
    tableData.value = result.list
    total.value = result.total
  } catch (error) {
    notify('接口调用失败', 'error')
  }
}

watch(
  [currentPage, pageSize],
  async () => {
    await getList()
  }
)

onMounted(async() => {
  await getList()
})

const handlePreview = (taskId: string) => {
  router.push(`/task/${taskId}`)
}
</script>

<template>
  <el-row class="row-bg" justify="end">
    <el-upload
      v-model:file-list="fileList"
      :limit="1"
      :auto-upload="false"
      :on-change="handleFileChange"
      :show-file-list="false"
    >
      <el-button type="primary" round>
        上传文件
      </el-button>
    </el-upload>
  </el-row>

  <el-row>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="task_id" label="任务ID" min-width="300" />
      <el-table-column prop="status" label="状态" min-width="100" />
      <el-table-column prop="created_at" label="创建时间" min-width="200" />
      <el-table-column label="操作" min-width="150">
        <template #default="scope">
          <el-button type="primary" link @click="handlePreview(scope.row.task_id)">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-row>
  <br>
  <el-row justify="end">
    <el-pagination
      v-model:current-page="currentPage"
      v-model:page-size="pageSize"
      :page-sizes="[10, 25, 50, 100]"
      :size="size"
      :disabled="disabled"
      :background="background"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
    />
  </el-row>
</template>
