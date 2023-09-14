<template>
<div>
  <el-card class="box-card top_card_sty" shadow="never">
    <div slot="header" class="clearfix">
      <span style="color: #666; font-size: 20px">我的项目</span>
      <el-input suffix-icon="el-icon-search" placeholder="搜索" size="small" style="float: right;width: 200px"></el-input>
    </div>
    <div>
      <el-tabs v-model="activeName">
        <el-tab-pane label="进行中的项目" name="进行中的项目">
          <el-row :gutter="30">
            <el-col :span="4" v-for="i in 6" :key="i" style="margin-bottom: 20px">
              <el-card shadow="hover" :body-style="{ padding:'10px' }" class="point">
                <el-image :src="require('../assets/项目默认封面.jpg')" class="card_img"></el-image>
                <div style="padding: 5px;">
                  <span>项目名称</span>
                  <div class="bottom clearfix">
                    <span class="card_createTime">创建时间</span>
                    <el-button class="el-icon-right button" type="text"></el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
            <el-col :span="4" style="margin-bottom: 20px">
              <el-card shadow="hover" :body-style="{ padding:'10px' }" class="point">
                <el-image :src="require('../assets/项目页新增图标.png')" style="background: #EBEEF5;" @click="setVisible"></el-image>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="已完成的项目" name="已完成的项目">
          <el-row :gutter="30">
            <el-col :span="4" v-for="i in 10" :key="i" style="margin-bottom: 20px">
              <el-card shadow="hover">
                ceshi
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </div>
  </el-card>
  <ProjectAddDialog
    :vs="dialogVisible"
    @getVisible="getVisible"
  ></ProjectAddDialog>
</div>
</template>

<script>
  import ProjectAddDialog from "../components/dialog/ProjectAddDialog.vue";

  export default {
    components: {ProjectAddDialog},
    data() {
      return {
        activeName: '进行中的项目',
        dialogVisible:false,
        activeProject:[],
        closedProject:[],
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      getVisible(val) {
        this.dialogVisible=val
      },
      setVisible() {
        this.dialogVisible = true
      }
    }
  };
</script>

<style scoped>
/deep/ .el-tabs__nav-wrap::after {
  content: "";
  left: 0;
  bottom: 0;
  position:relative;
  width: 100%;
  height: 2px;
  background-color: #E4E7ED;
  z-index: 1;
}
.top_card_sty{
  padding: 10px;
}
.card_img {
  width: 100%;
  height: 160px;
}
.card_createTime {
  font-size: 14px;
  color: #999;
}
.bottom{
  margin-top: 13px;
  line-height: 12px;
}
.button {
  float: right;
  padding: 0;
}
.point {
  cursor: pointer;
}
</style>
