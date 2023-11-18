<template>
  <div>
    <el-dialog :visible.sync="dialogVisible" @close="dialogVisible=false;sendVisible();clearForm()">
      <template slot="title">
        <div class="dialog_titleSty" v-if="type==='add'">新建项目</div>
        <div class="dialog_titleSty" v-else-if="type==='edit'">编辑项目</div>
        <el-divider></el-divider>
      </template>
      <el-form :model="projectData" ref="form">
        <el-form-item>
          <span class="el-icon-menu dialog_span">项目模版</span>
        </el-form-item>
        <el-form-item>
          <span class="el-icon-menu dialog_span">项目信息</span>
        </el-form-item>
        <el-row :gutter="30">
          <el-col :span="12">
            <el-form-item label="项目部门" prop="dept">
              <SelectTree
                ref="selectTree"
                :multipleType="multipleType"
                :pickedDept="projectData.dept"
                @getPid="getPid"
              >
              </SelectTree>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="项目成员" prop="member">
              <el-select
                v-model="projectData.member"
                multiple
                size="small"
              >
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item prop="name">
          <el-input placeholder="请输入项目名称" show-word-limit maxlength="15" v-model="projectData.name"></el-input>
        </el-form-item>
        <el-form-item prop="desc">
          <el-input type="textarea" placeholder="项目描述" show-word-limit maxlength="100" v-model="projectData.desc"></el-input>
        </el-form-item>
        <el-divider></el-divider>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" type="primary" v-if="type==='add'" @click="dialogVisible=false;sendVisible();creatProject()">创建</el-button>
        <el-button size="small" type="primary" v-else-if="type==='edit'" @click="dialogVisible=false;sendVisible();editProject()">确认</el-button>
        <el-button size="small" @click="dialogVisible=false;sendVisible()">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import SelectTree from "../../sys_child_page/SelectTree.vue";
import {data} from "autoprefixer";

export default {
  props:['vs','type','projectValue'],
  components: {SelectTree},
  watch:{
    vs(newValue) {
      if (newValue===true) {
        this.dialogVisible = true
        this.multipleType = true
      }
    },
    type(newValue) {
      if (newValue) {
        this.nowType=this.type
        console.log(this.nowType)
      }
    },
    projectValue(newValue) {
      if (newValue) {
        this.projectData = this.projectValue
        this.$refs.selectTree.checkedNodes(eval(this.projectData.dept))
        this.$refs.selectTree.getNodes()
      }
    },
  },
  data() {
    return{
      dialogVisible:false,
      multipleType:false,
      nowType:'',
      projectData:{
        name:'',
        desc:'',
        dept:'',
        member:[],
        status:'',
        createTime:'',
      },
      options:[],
    }
  },
  methods:{
    sendVisible(){
      this.$emit('getVisible','false')
    },
    clearForm() {
      this.$refs.form.resetFields()
    },
    // 获取子组件传递的部门ID
    getPid(id) {
      this.projectData.dept=id
      const arr = []
      // 通过部门ID给部门成员下拉框赋值
      for (let key in id) {
        this.$axios.get('api/emp/info/',{
          params:{id:id[key],name:''}
        }).then((response)=>{
          const res = response.data
          if (res['list'].length>0) {
            for (let k in res['list']){
              const dict = {}
              dict['value'] = res['list'][k]['id']
              dict['label'] = res['list'][k]['name']
              arr.push(dict)
            }
          }
        })
      }
      this.options = arr
    },
    creatProject() {
      this.projectData.status='进行中'
      this.projectData.createTime = new Date().toISOString().substring(0, 10)
      this.$axios.post('api/project/add/',{
        form:this.projectData
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('新增成功')
          location.reload()
        }else {
          this.$message.error('新增失败')
          console.log(res['respMsg'])
        }
      })
    },
    editProject() {
      this.$axios.post('api/project/edit/',{
        form:this.projectData
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.$message.success('编辑成功')
        }else {
          this.$message.error('编辑失败')
          console.log(res['respMsg'])
        }
      })
    }
  }
}
</script>

<style scoped>
/deep/ .el-dialog {
  border-radius: 10px;
}
/deep/ .el-dialog__body {
  padding: 0 20px;
}
.dialog_span{
  font-size: 20px;
  font-family: 微软雅黑,serif;
}
.button_div {
  float: right;
}
.dialog_titleSty {
  font-family: 微软雅黑,serif;
}
.el-divider {
  margin: 10px;
}
</style>
