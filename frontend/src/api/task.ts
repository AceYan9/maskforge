import request from '@/utils/request'

export interface UploadResult {
  task_id: number
}

export interface TaskInfo {
  task_id: number
  status: string
  created_at: string
}

export interface TaskListResult {
  list: TaskInfo[]
  page: number
  page_size: number
  total: number
  total_page: number
}

export interface TaskListParams {
  page: number
  page_size: number
}

export interface TaskDetail {
  status: string
  filename?: string
  rows?: number
  sample_data?: any[]
  columns?: string[]
  rules?: Record<string, any>
  date_columns?: string[]
  time_columns?: string[]
}

// 上传文件
export function uploadFile(file: any): Promise<UploadResult> {
  const formData = new FormData()
  formData.append('file', file)

  return request.post('/v1/tasks/', formData)
}

// 获取task列表
export function getTaskList(params: TaskListParams): Promise<TaskListResult> {
  return request.get('/v1/tasks/', {
    params,
  })
}

// 获取task详情
export function getTaskDetail(taskId: string): Promise<TaskDetail> {
  return request.get(`/v1/tasks/${taskId}/`)
}

// 数据预览
export function rulePreview(taskId: string, rules: Record<string, object>): Promise<object[]> {
  return request.post(`/v1/tasks/${taskId}/preview/`, rules)
}
