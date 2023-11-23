<script>
export default {
  data() {
    return{
      type:1,
      pid:'',
      rid:'',
      activeIndex:-1,
      dialogVisible:false,
      allIterationData:[],
      activeIterationData:{
        title:'',
        state:'',
        start:'',
        end:'',
      },
      activeRequirementData:[],
      formData:{
        title:'',
        state:'打开',
        start:'',
        end:'',
      },
      defaultFormData:{
        title:'',
        state:'打开',
        start:'',
        end:'',
      },
      formRules: {
        title:[{required: true, message:'请输入迭代名称', tigger:'blur'}],
        start:[{required: true, message:'请选择开始时间', tigger:'change'}],
        end:[{required: true, message:'请选择结束时间', tigger:'change'}],
      },
    }
  },
  created() {
    this.pid = sessionStorage.getItem('pid')
  },
  mounted() {
    this.getIterationData()
  },
  methods:{
    // 重置form表单数据
    clearForm() {
      // this.$refs['formData'].resetFields()
      this.$nextTick(()=>{
        this.$refs['formData'].clearValidate()
      })
      this.formData= Object.assign({},this.defaultFormData)
    },
    // 激活迭代页面
    activeCard(index,item) {
      this.activeIndex=index
      this.activeIterationData = item
      // 获取该迭代的需求数据
      this.$axios.get('api/project/requirement/info/',{
        params:{iterationId:item.id}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.activeRequirementData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 获取迭代数据
    getIterationData() {
      this.$axios.get('api/project/iteration/info/',{
        params:{pid:this.pid}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.allIterationData = res['list']
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
    // 提交表单
    submitForm(formName,rid) {
      this.$refs[formName].validate((valid)=>{
        if (valid) {
          if (this.type===1) {
            this.$axios.post('api/project/iteration/add/',{
              form:this.formData,pid:this.pid
            }).then((response)=>{
              const res = response.data
              if (res['respCode']==='000000') {
                this.$message.success('新增成功')
                this.getIterationData()
              }else {
                this.$message.error(res['respMsg'])
              }
            })
          }else {
            this.$axios.post('api/project/iteration/edit/',{
              form:this.formData,rid:rid
            }).then((response)=>{
              const res = response.data
              if (res['respCode']==='000000') {
                this.$message.success('修改成功')
                this.getIterationData()
              }else {
                this.$message.error(res['respMsg'])
              }
            })
          }
        }else {
          this.$message.error('请输入必填项')
          return false
        }
      })
    },
    // 编辑或删除迭代
    handleCommand(command) {
      console.log(this.rid)
      if (command==='edit') {
        this.type=2
        this.dialogVisible=true
      }else {
        this.$confirm('确定删除该迭代吗？',{
          confirmButtonText:'确定',
          cancelButtonText:'取消',
          type:"warning"
        }).then(()=>{
          this.$axios.delete('api/project/iteration/del/',{
            params:{rid:this.rid}
          }).then((response)=>{
            const res = response.data
            if (res['respCode']==='000000') {
              this.$message.success('删除成功')
              this.getIterationData()
            }else {
              this.$message.error(res['respMsg'])
            }
          })
        })
      }
    },
  },
}
</script>

<template>
  <div>
    <el-row :gutter="10">
      <el-col :span="6">
        <el-card shadow="never" class="left_card">
          <div slot="header">
            <el-button size="small" type="text" icon="el-icon-circle-plus-outline" @click="dialogVisible=true;type=1">创建迭代</el-button>
          </div>
          <div slot-scope="scope">
            <el-card
              v-for="(item,index) in allIterationData"
              :key="item.id" shadow="hover"
              style="margin-bottom: 10px"
              :class="{active:activeIndex===index}"
              class="point left_in_card_style"
              @click.native="activeCard(index,item)">
              <div>
                <span>{{ item.title }}</span>
                <el-dropdown @command="handleCommand" style="float: right">
                  <span class="el-dropdown-link">
                    <i class="el-icon-more el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="edit" icon="el-icon-edit" @click.native="rid=item.id;formData=item">编辑</el-dropdown-item>
                    <el-dropdown-item command="del" icon="el-icon-delete" @click.native="rid=item.id">删除</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
              <div>
                <span style="font-size: 12px;color: #999999">{{ item.start }} ~ {{ item.end }}</span>
                <el-divider></el-divider>
              </div>
              <div><el-progress :percentage="50" status="success"></el-progress></div>
            </el-card>
          </div>
        </el-card>
      </el-col>
      <el-col :span="18">
        <div style="margin-bottom: 10px">
          <el-card shadow="never" class="right_top_card">
            <div v-if="activeIterationData.title">
              <span style="color: #999999;font-size: 18px">{{ activeIterationData.title }}</span>
              <el-button size="mini" style="border-radius: 40px;margin: 0 20px" type="primary" plain>{{ activeIterationData.state }}</el-button>
              <span style="font-size: 12px;color: #999999">{{ activeIterationData.start }} ~ {{ activeIterationData.end }}</span>
            </div>
          </el-card>
        </div>
        <div>
          <el-card shadow="never" style="height: 68vh">
            <el-table :data="activeRequirementData" max-height="58vh" style="width: 100%;">
              <el-table-column
                label="#"
                type="index"
                width="80"
                align="align">
              </el-table-column>
              <el-table-column
                label="标题"
                prop="title">
              </el-table-column>
              <el-table-column
                label="优先级"
                prop="priority">
                <div slot-scope="scope">
                  <el-tag effect="dark" v-if="scope.row.priority==='紧急'" type="danger" size="small">{{ scope.row.priority }}</el-tag>
                  <el-tag effect="dark" v-else-if="scope.row.priority==='高'" type="warning" size="small">{{ scope.row.priority }}</el-tag>
                  <el-tag effect="dark" v-else-if="scope.row.priority==='中'" type="success" size="small">{{ scope.row.priority }}</el-tag>
                  <el-tag effect="dark" v-else type="info" size="small">{{ scope.row.priority }}</el-tag>
                </div>
              </el-table-column>
              <el-table-column
                label="状态"
                prop="state">
              </el-table-column>
              <el-table-column
                label="处理人"
                prop="handler">
              </el-table-column>
              <el-table-column
                label="预计开始"
                prop="start">
              </el-table-column>
              <el-table-column
                label="预计结束"
                prop="end">
              </el-table-column>
            </el-table>
          </el-card>
        </div>
      </el-col>
    </el-row>
    <div>
      <div>
        <el-dialog :visible="dialogVisible" @close="dialogVisible=false;clearForm()">
          <div slot="title">
            <span v-if="type===1">创建迭代</span>
            <span v-if="type===2">修改迭代</span>
            <el-divider></el-divider>
          </div>
          <div>
            <el-form :model="formData" ref="formData" :rules="formRules" inline>
              <el-form-item label="迭代名称" prop="title">
                <el-input placeholder="请输入迭代名称" size="small" v-model="formData.title"></el-input>
              </el-form-item>
              <el-form-item label="迭代状态" prop="state">
                <el-radio v-model="formData.state" label="打开">打开</el-radio>
                <el-radio v-model="formData.state" label="关闭">关闭</el-radio>
              </el-form-item>
              <el-form-item label="开始时间" prop="start">
                <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" size="small" v-model="formData.start"></el-date-picker>
              </el-form-item>
              <el-form-item label="结束时间" prop="end">
                <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" size="small" v-model="formData.end"></el-date-picker>
              </el-form-item>
            </el-form>
          </div>
          <div slot="footer">
            <el-button v-if="type===1" size="small" type="primary" @click="submitForm('formData');dialogVisible=false;clearForm()">创建</el-button>
            <el-button v-if="type===2" size="small" type="primary" @click="submitForm('formData',rid);dialogVisible=false;clearForm()">修改</el-button>
            <el-button size="small" @click="dialogVisible=false;clearForm()">取消</el-button>
          </div>
        </el-dialog>
      </div>
    </div>
  </div>
</template>

<style scoped>
.el-button--text {
  color: #999999;
}
.el-form-item {
  width:48%
}
.active {
  background-color: #d4e4ff;
}
.point {
  cursor: pointer;
}
.left_card {
  height: 76vh;
  overflow:auto;
}
.left_in_card_style {
  .el-divider .el-divider--horizontal {
    margin: 5px 0;
  }
  .el-card__header{
    padding: 10px 20px;
  }
}
.right_top_card {
  .el-card__body, .el-main {
    padding: 10px 20px;
  }
  min-height: 40px;
}
</style>
