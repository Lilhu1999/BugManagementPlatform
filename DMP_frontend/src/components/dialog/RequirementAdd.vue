<script>
export default {
  props:['vs'],
  data() {
    return {
      dialogVisible:false,
      form: {
        title:'',
        priority:'',
        iteration:'',
        state:'',
        handler:'',
        start:'',
        end:'',
        desc:'',
      },
      iterationOption:[
        {
          value: 'v4.1.6',
          label: 'v4.1.6'
        },{
          value: 'v4.1.7',
          label: 'v4.1.7'
        }
      ],
      priorityOption:[
        {
          value: '紧急',
          label: '紧急',
        },{
          value: '高',
          label: '高',
        },{
          value: '中',
          label: '中',
        },{
          value: '低',
          label: '低',
        }
      ]
    }
  },
  watch:{
    vs(newValue) {
      if (newValue) {
        this.dialogVisible=newValue
      }
    }
  },
  methods:{
    setVs() {
      this.$emit('getVs',false)
    }
  },
}
</script>

<template>
<div>
  <el-dialog :visible="dialogVisible" width="80%" destroy-on-close @close="dialogVisible = false;setVs()">
    <div slot="title">
      <span>创建工作项</span>
      <el-divider style="margin: 24px 0 0 0"></el-divider>
    </div>
    <el-form v-model="form">
      <el-row :gutter="30">
        <el-col :span="16">
          <div>
            <div>
              <el-form-item style="margin-bottom: 0">
                <el-input v-model="form.title" size="small" placeholder="请输入标题" class="title_input"></el-input>
              </el-form-item>
            </div>
            <div>
              <el-divider class="title_divider"></el-divider>
            </div>
            <div>
              <el-form-item>
                <el-input v-model="form.desc" type="textarea" :rows="10" placeholder="请输入内容" class="desc_input"></el-input>
              </el-form-item>
            </div>
          </div>
        </el-col>
        <el-col :span="1">
          <el-divider direction="vertical"></el-divider>
        </el-col>
        <el-col :span="7">
          <div>
            <div>
              <el-form-item label="迭代">
                <el-select v-model="form.iteration" size="small" class="right_input_width">
                  <el-option
                    v-for="item in iterationOption"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="优先级">
                <el-select v-model="form.priority" size="small" class="right_input_width">
                  <el-option
                    v-for="item in priorityOption"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="处理人">
                <el-input v-model="form.handler" size="small" class="right_input_width"></el-input>
              </el-form-item>
              <el-form-item label="预计开始">
                <el-date-picker v-model="form.start" type="date" size="small" class="right_input_width"></el-date-picker>
              </el-form-item>
              <el-form-item label="预计结束">
                <el-date-picker v-model="form.end" type="date" size="small" class="right_input_width"></el-date-picker>
              </el-form-item>
            </div>
          </div>
        </el-col>
        <el-col :span="24">
          <el-divider></el-divider>
        </el-col>
        <el-col :span="24">
          <el-button size="small" type="primary">创建</el-button>
          <el-button size="small">取消</el-button>
        </el-col>
      </el-row>
    </el-form>
  </el-dialog>
</div>
</template>

<style scoped>
/deep/ .el-form-item__label {
  width: 80px;
  text-align: left;
}
/deep/ .right_input_width {
  width: 200px;
}
.title_input /deep/ .el-input__inner{
  border:none;
}
.title_divider {
  margin: 0 0 20px 0;
  width: 100%;
}
.el-divider--vertical{
  height: 40vh;
}
</style>
