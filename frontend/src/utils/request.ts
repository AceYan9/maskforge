import axios, {
  type AxiosError,
  type AxiosRequestConfig,
  type AxiosResponse,
} from 'axios'
import { notify } from '@/utils/notification'

/**
 * 后端统一响应结构
 */
export interface ApiResponse<T> {
  code: number
  data: T
  message: string
}

/**
 * Axios 实例
 */
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 30000,
})

/**
 * 请求拦截器
 */
service.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

/**
 * 响应拦截器
 *
 * 注意：
 * 这里不要 return response.data.data
 * 否则 Axios 的类型会和 AxiosResponse 冲突。
 *
 * 这里只负责：
 * 1. 判断后端 code
 * 2. 统一处理业务错误
 * 3. 统一处理 HTTP 错误
 *
 * 真正的数据解包在下面 request.get/post/put/delete 中完成。
 */
service.interceptors.response.use(
  (response: AxiosResponse) => {
    const result = response.data as ApiResponse<unknown>

    if (result.code !== 0) {
      notify(result.message)
      return Promise.reject(new Error(result.message))
    }

    return response
  },
  (error: AxiosError) => {
    if (error.response) {
      const status = error.response.status

      switch (status) {
        case 401:
          localStorage.removeItem('access_token')
          notify('登录已过期，请重新登录', 'error')
          break

        case 403:
          notify('没有权限', 'error')
          break

        case 404:
          notify('请求资源不存在', 'error')
          break

        case 422:
          notify('请求参数错误', 'error')
          break

        case 500:
          notify('服务器异常', 'error')
          break

        default:
          notify(
            getErrorMessage(error.response.data) || '请求失败',
            'error',
          )
          break
      }
    } else if (error.request) {
      notify('网络请求失败，请检查网络连接', 'error')
    } else {
      notify(error.message || '请求失败', 'error')
    }

    return Promise.reject(error)
  },
)

/**
 * 获取后端错误信息
 */
function getErrorMessage(data: unknown): string | undefined {
  if (!data || typeof data !== 'object') {
    return undefined
  }

  if ('message' in data && typeof data.message === 'string') {
    return data.message
  }

  if ('detail' in data && typeof data.detail === 'string') {
    return data.detail
  }

  return undefined
}

/**
 * 对外暴露的 request
 *
 * 这里负责把：
 *
 * AxiosResponse<ApiResponse<T>>
 *
 * 转换成：
 *
 * T
 */
const request = {
  /**
   * GET
   */
  async get<T>(
    url: string,
    config?: AxiosRequestConfig,
  ): Promise<T> {
    const response = await service.get<ApiResponse<T>>(
      url,
      config,
    )

    return response.data.data
  },

  /**
   * POST
   */
  async post<T>(
    url: string,
    data?: unknown,
    config?: AxiosRequestConfig,
  ): Promise<T> {
    const response = await service.post<ApiResponse<T>>(
      url,
      data,
      config,
    )

    return response.data.data
  },

  /**
   * PUT
   */
  async put<T>(
    url: string,
    data?: unknown,
    config?: AxiosRequestConfig,
  ): Promise<T> {
    const response = await service.put<ApiResponse<T>>(
      url,
      data,
      config,
    )

    return response.data.data
  },

  /**
   * DELETE
   */
  async delete<T>(
    url: string,
    config?: AxiosRequestConfig,
  ): Promise<T> {
    const response = await service.delete<ApiResponse<T>>(
      url,
      config,
    )

    return response.data.data
  },
}

export default request
