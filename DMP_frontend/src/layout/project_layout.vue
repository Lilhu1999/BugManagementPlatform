<script>
export default {
  data() {
    return{
      activePath:'',
      projectData:[{
        name:'',
      }],
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
      // 将项目ID存储于会话中，命名为pid
      sessionStorage.setItem('pid',this.projectData[0]['id'])
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
  <el-container>
    <el-header>
      <el-menu
        router
        :default-active="activePath"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        active-text-color="#409EFF"
        >
        <el-menu-item class="header-project-name">
          <div>
            <el-icon class="el-icon-s-order"></el-icon>
            <span>{{ projectData[0]['name'] }}</span>
          </div>
        </el-menu-item>
        <el-menu-item index="/pj/requirement" @click="saveActivePath('/pj/requirement')">需求</el-menu-item>
        <el-menu-item index="/pj/defect" @click="saveActivePath('/pj/defect')">缺陷</el-menu-item>
        <el-menu-item index="/pj/testCase" @click="saveActivePath('/pj/testCase')">测试用例</el-menu-item>
        <el-menu-item index="/pj/document" @click="saveActivePath('/pj/document')">文档</el-menu-item>
        <el-menu-item index="/pj/iteration" @click="saveActivePath('/pj/iteration')">迭代</el-menu-item>
        <el-menu-item style="float: right">
          <el-input v-model="searchInput" class="header_input" prefix-icon="el-icon-search" size="small"></el-input>
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
  </el-container>
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
