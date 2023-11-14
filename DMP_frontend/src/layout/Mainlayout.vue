<template>
  <div class="back_sty">
  <el-container>
    <el-aside width="60px">
      <div>
        <el-menu
          router
          :collapse="true"
          :default-active="activePath"
          class="el-menu-vertical-demo"
          style="width: 60px"
          @open="handleOpen"
          @close="handleClose"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item>
            logo
          </el-menu-item>
          <el-menu-item index="/home" @click="saveActivePath('/home')">
            <i class="el-icon-monitor el_menu_i_sty"></i>
            <div class="el_menu_text_sty">
              工作台
            </div>
          </el-menu-item>
          <el-menu-item index="/document" @click="saveActivePath('/document')">
            <i class="el-icon-folder el_menu_i_sty"></i>
            <div class="el_menu_text_sty">
              文档
            </div>
          </el-menu-item>
          <el-menu-item index="/project" @click="saveActivePath('/project')">
            <i class="el-icon-document el_menu_i_sty"></i>
            <div class="el_menu_text_sty">
              项目
            </div>
          </el-menu-item>
          <el-menu-item index="/autoTest" @click="saveActivePath('/autoTest')">
            <i class="el-icon-cpu el_menu_i_sty"></i>
            <div class="el_menu_text_sty">
              自动化
            </div>
          </el-menu-item>
          <el-menu-item index="/setting" @click="saveActivePath('/setting')">
            <i class="el-icon-setting el_menu_i_sty"></i>
            <div class="el_menu_text_sty">
              系统设置
            </div>
          </el-menu-item>
          <div class="aside_avatar">
            <el-dropdown @command="handleCommand">
              <el-avatar>{{ this.$cookies.get('username').slice(0,1) }}</el-avatar>
              <el-dropdown-menu>
                <el-dropdown-item command="editPassword">修改密码</el-dropdown-item>
                <el-dropdown-item command="exit">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </el-menu>
      </div>
    </el-aside>
    <el-container>
      <el-main>
        <router-view></router-view>
      </el-main>
      <el-footer>
        <div class="footer_div">Copyright © By Lil_hu版权所有</div>
        <el-link href="https://beian.miit.gov.cn/" target="_blank">浙ICP备2023040189号-1</el-link>
      </el-footer>
    </el-container>
  </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activePath:'',
    }
  },
  methods: {
    saveActivePath(activePath) {
      sessionStorage.setItem('activePath',activePath)
      this.activePath=activePath
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleCommand(command) {
      if (command==='editPassword') {
        this.$message.info('待开发')
      }else {
        this.$cookies.remove('username')
        this.$cookies.remove('user_type')
        this.$router.push('/login')
      }
    },
  }
}
</script>
<style scoped>
.el-main {
  background: #EBEEF5;
  padding: 0;
  overflow-x: hidden;
  border-radius: 0 10px 10px 0;
  height: 80vh;
}
.el-aside {
  border-radius:10px 0 0 10px;
  overflow-x: hidden;
}
.el-menu {
  height: 97vh;
}
.el-footer {
  background-color: #EBEEF5;
  text-align: center;
}
.el-menu-item {
  line-height: 40px;
  height: 80px;
}
.el_menu_i_sty{
  width: 60px !important;
  height: 20px;
  position: relative;
  left: -20px;
}
.el_menu_text_sty{
  width: 60px;
  height: 40px;
  text-align: center;
  position: relative;
  left: -20px;
  top: -10px
}
.aside_avatar {
  text-align: center;
  margin-top: 200px;
}
.footer_div{
  font-size: 12px;
  color: #999999;
}
</style>
