<template>
  <div>
    <el-dialog :visible.sync="dialogVisible">
      <template slot="title">
        <div class="dialog_titleSty">新建项目</div>
        <el-divider></el-divider>
      </template>
      <el-form :model="projectData">
        <el-form-item>
          <span class="el-icon-menu dialog_span">项目模版</span>
        </el-form-item>
        <el-form-item>
          <span class="el-icon-menu dialog_span">项目信息</span>
        </el-form-item>
        <el-row :gutter="30">
          <el-col :span="12">
            <el-form-item label="项目部门">
              <SelectTree
                :multipleType="multipleType"
                @getPid="getPid"
              >
              </SelectTree>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="项目成员">
              <el-select
                v-model="projectData.value"
                multiple
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
        <el-form-item>
          <el-input placeholder="请输入项目名称" show-word-limit maxlength="15" v-model="projectData.name"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="textarea" placeholder="项目描述" show-word-limit maxlength="100" v-model="projectData.desc"></el-input>
        </el-form-item>
        <el-divider></el-divider>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" type="primary" @click="dialogVisible=false;sendVisible();creatProject()">创建</el-button>
        <el-button size="small" @click="dialogVisible=false;sendVisible()">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import SelectTree from "../../sys_child_page/SelectTree.vue";

export default {
  props:['vs'],
  components: {SelectTree},
  watch:{
    vs(newValue) {
      if (newValue===true) {
        this.dialogVisible = true
        this.multipleType = true
      }
    }
  },
  data() {
    return{
      dialogVisible:false,
      multipleType:false,
      projectData:{
        name:'',
        desc:'',
        value:[],
      },
      options:[],
    }
  },
  methods:{
    sendVisible(){
      this.$emit('getVisible','false')
    },
    // 获取子组件传递的部门ID
    getPid(id) {
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

    },
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
