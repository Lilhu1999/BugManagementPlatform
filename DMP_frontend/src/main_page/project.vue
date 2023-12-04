<template>
<div>
  <el-card class="box-card top_card_sty" shadow="never">
    <div slot="header" class="clearfix">
      <span style="color: #666; font-size: 20px">我的项目</span>
      <el-input suffix-icon="el-icon-search" placeholder="搜索" size="small" style="float: right;width: 200px"></el-input>
    </div>
    <div>
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="进行中的项目" name="进行中的项目">
          <el-row :gutter="30">
            <el-col :span="4" v-for="item in activeProject" :key="item" style="margin-bottom: 10px">
              <el-card shadow="hover" :body-style="{ padding:'10px' }" class="point">
                <el-image :src="require('../assets/项目默认封面.jpg')" class="card_img"></el-image>
                <div style="padding: 5px;">
                  <span>{{ item.name }}</span>
                  <div class="bottom clearfix">
                    <span class="card_createTime">{{ item.createTime }}</span>
                    <el-button class="el-icon-right button" type="text" @click="toPath(item.id)"></el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
            <el-col :span="4" style="margin-bottom: 20px" v-if="$cookies.get('user_type')==='管理员'">
              <el-card shadow="hover" :body-style="{ padding:'10px' }" class="point add_card">
                <el-icon class="el-icon-circle-plus-outline add_card_icon" @click="setVisible"></el-icon>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="已完成的项目" name="已完成的项目">
          <el-row :gutter="30">
            <el-col :span="4" v-for="item in activeProject" :key="item" style="margin-bottom: 10px">
              <el-card shadow="hover" :body-style="{ padding:'10px' }" class="point">
                <el-image :src="require('../assets/项目默认封面.jpg')" class="card_img"></el-image>
                <div style="padding: 5px;">
                  <span>{{ item.name }}</span>
                  <div class="bottom clearfix">
                    <span class="card_createTime">{{ item.createTime }}</span>
                    <el-button class="el-icon-right button" type="text"></el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </div>
  </el-card>
  <router-view></router-view>
  <ProjectAddDialog
    :vs="dialogVisible"
    :type="type"
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
        status:'',
        type:'add',
      };
    },
    mounted() {
      this.getAllProject()
    },
    methods: {
      toPath(id) {
        this.$router.push({
          name:'pj',
          query:{id:id},
        })
      },
      handleClick(el) {
        this.activeName = el.name
        this.getAllProject()
      },
      getVisible(val) {
        this.dialogVisible=val
      },
      setVisible() {
        this.dialogVisible = true
      },
      // 获取项目数据
      getAllProject() {
        if (this.activeName==='进行中的项目') {
          this.status = '进行中'
        }else {
          this.status = '已完成'
        }
        this.$axios.get('api/project/info/',{
          params:{status:this.status}
        }).then((response)=>{
          const res = response.data
          if (res['respCode']==='000000'){
            this.activeProject = res['list']
            console.log(this.activeProject)
          }else {
            console.log(res['respMsg'])
          }
        })
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
.add_card{
  display: flex;
  width: 160px;
  height: 160px;
  justify-content: center;
  align-items: center;
}
.add_card_icon {
  font-size: 8vh;
  color: #8cc5ff;
}
</style>
