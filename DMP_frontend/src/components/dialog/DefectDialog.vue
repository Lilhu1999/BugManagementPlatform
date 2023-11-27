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
        creator:'',
        importance:'',
        createTime:'',
        desc:'',
      },
      defaultFrom:{
        title:'',
        priority:'',
        iteration:'',
        state:'',
        handler:'',
        creator:'',
        importance:'',
        createTime:'',
        desc:'',
      },
      iterationOption:[],
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
      ],
      importanceOption:[
        {
          value: '致命',
          label: '致命',
        },{
          value: '严重',
          label: '严重',
        },{
          value: '一般',
          label: '一般',
        },{
          value: '建议',
          label: '建议',
        }
      ],
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
  mounted() {
    this.getIterationData()
  },
  methods:{
    setVs() {
      this.$emit('getVs',false)
    },
    // 重置表单
    resetFrom() {
      this.form = Object.assign({},this.form,this.defaultFrom)
    },
    // 动态获取迭代数据
    async getIterationData() {
      let pid = await this.setPid()
      this.$axios.get('api/project/iteration/info/',{
        params:{pid:pid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.iterationOption = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    async setPid() {
      return sessionStorage.getItem('pid')
    },
    // pid即所属项目ID
    async createDefect() {
      let pid = await this.setPid()
      this.$axios.post('api/project/defect/add/',{
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
    editDefect(rid) {
      this.$axios.post('api/project/defect/edit/',{
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
      <span v-if="ea==='add'">创建缺陷</span>
      <span v-else-if="ea==='edit'">修改缺陷</span>
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
                <el-input v-model="form.desc" type="textarea" :rows="10" placeholder="请输入复现步骤" class="desc_input"></el-input>
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
              <el-form-item label="严重程度">
                <el-select v-model="form.importance" size="small" class="right_input_width">
                  <el-option
                    v-for="item in importanceOption"
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
              <el-form-item label="创建人">
                <el-input v-model="form.creator" size="small" class="right_input_width"></el-input>
              </el-form-item>
            </div>
          </div>
        </el-col>
        <el-col :span="24">
          <el-divider></el-divider>
        </el-col>
        <el-col :span="24" v-if="$cookies.get('user_type')==='管理员'">
          <el-button size="small" type="primary" v-if="this.ea==='add'" @click="dialogVisible=false;createDefect();setVs()">创建</el-button>
          <el-button size="small" type="primary" v-else-if="this.ea==='edit'" @click="dialogVisible=false;editDefect(form.id);setVs()">修改</el-button>
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
