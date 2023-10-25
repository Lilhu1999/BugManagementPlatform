<script>
export default {
  data() {
    return{
      activePath:'',
      projectData:[],
      searchInput:'',
    }
  },
  mounted() {
    this.getProjectInfo(this.$route.query.id)
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    saveActivePath(activePath) {
      sessionStorage.setItem('activePath',activePath)
      this.activePath=activePath
    },
    getProjectInfo(id) {
      this.$axios.get('api/project/info/',{
        params:{id:id}
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000'){
          this.projectData = res['list']
          console.log(this.projectData)
        }else {
          console.log(res['respMsg'])
        }
      })
    }
  },
}
</script>

<template>
<div>
  <el-header>
    <el-menu
      :default-active="activePath"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      >
      <el-menu-item class="header-project-name">
        <div>
          <el-icon class="el-icon-s-order"></el-icon>
          <span>{{ projectData[0].name }}</span>
        </div>
      </el-menu-item>
      <el-menu-item index="/requirement" @click="saveActivePath('/requirement')">需求</el-menu-item>
      <el-menu-item index="/defect" @click="saveActivePath('/defect')">缺陷</el-menu-item>
      <el-menu-item index="/testCase" @click="saveActivePath('/testCase')">测试用例</el-menu-item>
      <el-menu-item style="float: right">
        <el-input v-model="searchInput" class="header_input" prefix-icon="el-icon-search" size="small"></el-input>
      </el-menu-item>
    </el-menu>
  </el-header>
  <el-main>
    <router-view></router-view>
  </el-main>
</div>
</template>

<style scoped>
.el-header {
  padding: 0;
}
.el-menu-item {
  padding:0 30px;
}
.header-project-name {
  padding-right: 100px;
}
.header_input {
  border-radius: 20px;
  width: 200px;
  padding: 0;
}
</style>
