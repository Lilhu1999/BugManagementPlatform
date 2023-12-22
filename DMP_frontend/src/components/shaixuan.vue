<script>
export default {
  data() {
    return {
      options: {
        priority: '全部',
        importance: '全部',
        state: '全部',
      },
    }
  },
  mounted() {
  },
  watch: {
    // 监听筛选项更新情况
    options:{
      handler(newValue){
        if (newValue) {
          this.sendData()
        }
      },
      deep: true,
      immediate: true,
    },
  },
  methods:{
    //发送数据给父组件
    sendData() {
      this.$emit('getSelectedData',this.options)
    },
    //设置对象属性
    setOptions(key,val) {
      this.$set(this.options,key,val)
    }
  },
}
</script>

<template>
<div>
  <el-popover trigger="hover">
    <div>
      <div>
        <div class="title_bottom"><span>优先级</span></div>
        <el-button-group>
          <el-button :type="options.priority==='全部'? 'primary':''" size="small" @click.native="setOptions('priority','全部')">全部</el-button>
          <el-button :type="options.priority==='紧急'? 'primary':''" size="small" @click.native="setOptions('priority','紧急')">紧急</el-button>
          <el-button :type="options.priority==='高'? 'primary':''" size="small" @click.native="setOptions('priority','高')">高</el-button>
          <el-button :type="options.priority==='中'? 'primary':''" size="small" @click.native="setOptions('priority','中')">中</el-button>
          <el-button :type="options.priority==='低'? 'primary':''" size="small" @click.native="setOptions('priority','低')">低</el-button>
        </el-button-group>
      </div>
      <el-divider></el-divider>
      <div>
        <div class="title_bottom"><span>严重程度</span></div>
        <el-button-group>
          <el-button :type="options.importance==='全部'? 'primary':''" size="small" @click.native="setOptions('importance','全部')">全部</el-button>
          <el-button :type="options.importance==='致命'? 'primary':''" size="small" @click.native="setOptions('importance','致命')">致命</el-button>
          <el-button :type="options.importance==='严重'? 'primary':''" size="small" @click.native="setOptions('importance','严重')">严重</el-button>
          <el-button :type="options.importance==='一般'? 'primary':''" size="small" @click.native="setOptions('importance','一般')">一般</el-button>
          <el-button :type="options.importance==='建议'? 'primary':''" size="small" @click.native="setOptions('importance','建议')">建议</el-button>
        </el-button-group>
      </div>
      <el-divider></el-divider>
      <div>
        <div class="title_bottom"><span>状态</span></div>
        <el-button-group>
          <el-button :type="options.state==='全部'? 'primary':''" size="small" @click.native="setOptions('state','全部')">全部</el-button>
          <el-button :type="options.state==='待修复'? 'primary':''" size="small" @click.native="setOptions('state','待解决')">待解决</el-button>
          <el-button :type="options.state==='已修复'? 'primary':''" size="small" @click.native="setOptions('state','已解决')">已解决</el-button>
          <el-button :type="options.state==='重新打开'? 'primary':''" size="small" @click.native="setOptions('state','重新打开')">重新打开</el-button>
          <el-button :type="options.state==='关闭'? 'primary':''" size="small" @click.native="setOptions('state','已关闭')">已关闭</el-button>
        </el-button-group>
      </div>
    </div>
    <el-icon class="el-icon-setting" slot="reference"></el-icon>
  </el-popover>
</div>
</template>

<style scoped>
.title_bottom {
  margin-bottom: 20px;
}
</style>
