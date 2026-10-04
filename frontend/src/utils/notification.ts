import { ElNotification } from 'element-plus'
import { CloseBold } from '@element-plus/icons-vue'

type NotifyType = 'primary' | 'success' | 'warning' | 'info' | 'error'

export function notify(message: string, messageType: NotifyType = 'info') {
  ElNotification({
    message,
    type: messageType,
    closeIcon: CloseBold,
    showClose: false,
  })
}