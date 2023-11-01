<script>
export default {
  props:['vs','ea','editForm'], //vs=>dialogVisible; ea=>editOrAdd
  data() {
    return {
      dialogVisible:false,
      pid:'',
      form: {
        title:'',
        type:'',
        level:'',
        creator:'',
        createTime:'',
        desc:'',
      },
      defaultFrom:{
        title:'',
        type:'',
        level:'',
        creator:'',
        createTime:'',
        desc:'',
      },
      level:[
        {
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
      type:[
        {
          value: '功能测试',
          label: '功能测试',
        },{
          value: '性能测试',
          label: '性能测试',
        },{
          value: '安全测试',
          label: '安全测试',
        },{
          value: '兼容性测试',
          label: '兼容性测试',
        },{
          value: '界面测试',
          label: '界面测试',
        },{
          value: '场景测试',
          label: '场景测试',
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
    async createTestCase() {
      let pid = await this.setPid()
      this.$axios.post('api/project/testcase/add/',{
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
    editTestCase(rid) {
      this.$axios.post('api/project/testcase/edit/',{
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
      <span v-if="ea==='add'">创建用例</span>
      <span v-else-if="ea==='edit'">修改用例</span>
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
              <el-form-item label="用例等级">
                <el-select v-model="form.level" size="small" class="right_input_width">
                  <el-option
                    v-for="item in level"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="用例类型">
                <el-select v-model="form.type" size="small" class="right_input_width">
                  <el-option
                    v-for="item in type"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
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
        <el-col :span="24">
          <el-button size="small" type="primary" v-if="this.ea==='add'" @click="dialogVisible=false;createTestCase();setVs()">创建</el-button>
          <el-button size="small" type="primary" v-else-if="this.ea==='edit'" @click="dialogVisible=false;editTestCase(form.id);setVs()">修改</el-button>
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
