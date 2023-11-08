<script>
export default {
  props:['vs','ea','editForm'], //vs=>dialogVisible; ea=>editOrAdd
  data() {
    return {
      dialogVisible:false,
      pid:'',
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
      defaultFrom:{
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
    },
    editForm(newValue) {
      if (newValue !== []) {
        this.form = newValue[0]
      }
    }
  },
  methods:{
    setVs() {
      this.$emit('getVs',false)
    },
    // 重置表单
    resetFrom() {
      this.form = Object.assign({},this.form,this.defaultFrom)
    },
    async setPid() {
      return sessionStorage.getItem('pid')
    },
    // pid即所属项目ID
    async createRequirement() {
      let pid = await this.setPid()
      this.$axios.post('api/project/requirement/add/',{
        form:this.form,pid:pid
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('新增成功')
          this.$emit('fresh',true)
          this.resetFrom()
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    editRequirement(rid) {
      this.$axios.post('api/project/requirement/edit/',{
        form:this.form,rid:rid
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('修改成功')
          this.$emit('fresh',true)
          this.resetFrom()
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
  },
}
</script>

<template>
<div>
  <el-dialog :visible="dialogVisible" width="80%" @close="dialogVisible = false;setVs();">
    <div slot="title">
      <span v-if="ea==='add'">创建工作项</span>
      <span v-else-if="ea==='edit'">修改工作项</span>
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
                <el-date-picker value-format="yyyy-MM-dd" v-model="form.start" type="date" size="small" class="right_input_width"></el-date-picker>
              </el-form-item>
              <el-form-item label="预计结束">
                <el-date-picker value-format="yyyy-MM-dd" v-model="form.end" type="date" size="small" class="right_input_width"></el-date-picker>
              </el-form-item>
            </div>
          </div>
        </el-col>
        <el-col :span="24">
          <el-divider></el-divider>
        </el-col>
        <el-col :span="24" v-if="$cookies.get('user_type')==='管理员'">
          <el-button size="small" type="primary" v-if="this.ea==='add'" @click="dialogVisible=false;createRequirement();setVs()">创建</el-button>
          <el-button size="small" type="primary" v-else-if="this.ea==='edit'" @click="dialogVisible=false;editRequirement(form.id);setVs()">修改</el-button>
          <el-button size="small" @click="dialogVisible=false;setVs();resetFrom()">取消</el-button>
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
