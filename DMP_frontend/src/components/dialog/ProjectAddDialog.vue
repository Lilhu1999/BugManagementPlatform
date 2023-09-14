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
            <el-form-item label="项目成员">
              <MemberCascader>
              </MemberCascader>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="项目管理员">
              <MemberCascader>
              </MemberCascader>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item>
          <el-input placeholder="请输入项目名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="textarea" placeholder="项目描述"></el-input>
        </el-form-item>
        <el-divider></el-divider>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" type="primary" @click="dialogVisible=false;sendVisible()">创建</el-button>
        <el-button size="small" @click="dialogVisible=false;sendVisible()">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import MemberCascader from "../MemberCascader.vue";

export default {
  props:['vs'],
  components: {MemberCascader},
  watch:{
    vs(newValue) {
      if (newValue===true) {
        this.dialogVisible = true
      }
    }
  },
  data() {
    return{
      dialogVisible:false,
      projectData:[],
    }
  },
  methods:{
    sendVisible(){
      this.$emit('getVisible','false')
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
