interface selectOption {
  label: string,
  value: string,
}

interface ruleField {
  key: string,
  label: string,
  type: string,
  options?: selectOption[],
  disabled?: boolean,
  allowNegative?: boolean,
}

interface ruleConfig {
  label: string,
  fields: ruleField[],
  isDate?: boolean,
  isTime?: boolean,
}

export const rulesConfig: Record<string, ruleConfig> = {
  none: {
    label: '不处理',
    fields: [],
  },
  left_mask: {
    label: '左侧掩码',
    fields: [
      {
        key: 'count',
        label: '掩码长度',
        type: 'number',
      },
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
      {
        key: 'anchor',
        label: '锚定字符',
        type: 'input',
      },
      {
        key: 'anchor_side',
        label: '掩码方向',
        type: 'select',
        options: [
          {label: '左侧', value: 'left'},
          {label: '右侧', value: 'right'},
        ]
      },
    ],
  },
  right_mask: {
    label: '右侧掩码',
    fields: [
      {
        key: 'count',
        label: '掩码长度',
        type: 'number',
      },
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
      {
        key: 'anchor',
        label: '锚定字符',
        type: 'input',
      },
      {
        key: 'anchor_side',
        label: '掩码方向',
        type: 'select',
        options: [
          {label: '左侧', value: 'left'},
          {label: '右侧', value: 'right'},
        ]
      },
    ],
  },
  middle_mask: {
    label: '中间掩码',
    fields: [
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
      {
        key: 'left_save_count',
        label: '左侧保留长度',
        type: 'number',
      },
      {
        key: 'right_save_count',
        label: '右侧保留长度',
        type: 'number',
      },
    ],
  },
  both_sides_mask: {
    label: '两侧掩码',
    fields: [
      {
        key: 'left_count',
        label: '左侧长度',
        type: 'number',
      },
      {
        key: 'right_count',
        label: '右侧长度',
        type: 'number',
      },
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
    ],
  },
  hash_mask: {
    label: 'Hash',
    fields: [
      {
        key: 'algorithm',
        label: '算法',
        type: 'select',
        options: [
          {label: 'MD5', value: 'md5'},
          {label: 'SHA1', value: 'sha1'},
          {label: 'SHA224', value: 'sha224'},
          {label: 'SHA256', value: 'sha256'},
          {label: 'SHA384', value: 'sha384'},
          {label: 'SHA512', value: 'sha512'},
          {label: 'SHA3_224', value: 'sha3_224'},
          {label: 'SHA3_256', value: 'sha3_256'},
          {label: 'SHA3_384', value: 'sha3_384'},
          {label: 'SHA3_512', value: 'sha3_512'},
        ]
      },
    ],
  },
  all_mask: {
    label: '全部掩码',
    fields: [
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
    ],
  },
  date_mask: {
    label: '日期掩码',
    isDate: true,
    fields: [
      {
        key: 'format',
        label: '格式',
        type: 'input',
        disabled: true,
      },
      {
        key: 'hides',
        label: '隐藏项',
        type: 'datetimeSelect',
        options: [
          {label: '年', value: 'YYYY'},
          {label: '月', value: 'MM'},
          {label: '日', value: 'DD'},
          {label: '时', value: 'HH'},
          {label: '分', value: 'mm'},
          {label: '秒', value: 'ss'},
        ]
      },
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
    ],
  },
  date_offset_mask: {
    label: '日期偏移',
    isDate: true,
    fields: [{
        key: 'format',
        label: '格式',
        type: 'input',
        disabled: true,
      },
      {
        key: 'date_offset.min',
        label: '偏移最小天数',
        type: 'number',
        allowNegative: true,
      },
      {
        key: 'date_offset.max',
        label: '偏移最大天数',
        type: 'number',
        allowNegative: true,
      },],
  },
  time_mask: {
    label: '时间掩码',
    isTime: true,
    fields: [
      {
        key: 'format',
        label: '格式',
        type: 'input',
        disabled: true,
      },
      {
        key: 'hides',
        label: '隐藏项',
        type: 'datetimeSelect',
        options: [
          {label: '年', value: 'YYYY'},
          {label: '月', value: 'MM'},
          {label: '日', value: 'DD'},
          {label: '时', value: 'HH'},
          {label: '分', value: 'mm'},
          {label: '秒', value: 'ss'},
        ]
      },
      {
        key: 'mask_char',
        label: '掩码字符',
        type: 'input',
      },
    ],
  },
  time_offset_mask: {
    label: '时间偏移',
    isTime: true,
    fields: [
      {
        key: 'format',
        label: '格式',
        type: 'input',
        disabled: true,
      },
      {
        key: 'time_offset.min',
        label: '偏移最小小时数',
        type: 'number',
        allowNegative: true,
      },
      {
        key: 'time_offset.max',
        label: '偏移最大小时数',
        type: 'number',
        allowNegative: true,
      },
    ],
  }
}

export const ruleDefaultConfig: Record<string, any> = {
  none: {},
  left_mask: {
    rule_type: 'left_mask',
    count: 3,
    mask_char: '*',
    anchor: '',
    anchor_side: '',
  },
  right_mask: {
    rule_type: 'right_mask',
    count: 3,
    mask_char: '*',
    anchor: '',
    anchor_side: '',
  },
  middle_mask: {
    rule_type: 'middle_mask',
    mask_char: '*',
    left_save_count: 1,
    right_save_count: 1,
  },
  both_sides_mask: {
    rule_type: 'both_sides_mask',
    left_count: 1,
    right_count: 1,
    mask_char: '*'
  },
  hash_mask: {
    rule_type: 'left_mask',
    algorithm: 'sha256',
  },
  all_mask: {
    rule_type: 'all_mask',
  },
  date_mask: {
    rule_type: 'date_mask',
    hides: [],
    mask_char: '*',
  },
  date_offset_mask: {
    rule_type: 'date_offset_mask',
    date_offset: {
      min: -5,
      max: 5,
    },
  },
  time_mask: {
    rule_type: 'time_mask',
    hides: [],
    mask_char: '*',
  },
  time_offset_mask: {
    rule_type: 'time_offset_mask',
    time_offset: {
      min: -5,
      max: 5,
    },
  }
}
