<script>
export default {
  data(){
    return{
      rules:{
        username:[{require:true,message:'请输入用户名',tigger:'blur'}],
        password:[{require:true,message:'请输入密码',tigger:'blur'}],
      },
      loginForm:{
        username:'',
        password:'',
      },
    };
  },
  methods:{
    login() {
      this.$axios.post('api/login/',{
        form:this.loginForm
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          sessionStorage.setItem('username',this.loginForm.username)
          sessionStorage.setItem('user_type',res['user_type'])
          this.$router.push({path:'/index'})
          this.$message.success('登录成功')
        }else {
          this.$message.error(res['respMsg'])
        }
      })
    },
  }
}
</script>

<template>
<div class="login">
  <div>
    <div>
      <el-card class="login_card">
        <div class="login_card_left">
          <div class="login_card_img">
          </div>
        </div>
        <div class="login_card_right">
          <div class="login_card_title"><span>测试管理平台demo用户登录</span></div>
          <div class="login_card_input">
            <el-form ref="loginForm" :model="loginForm" :rules="rules">
              <el-form-item prop="username">
                <el-input v-model="loginForm.username" prefix-icon="el-icon-user" placeholder="用户名" clearable></el-input>
              </el-form-item>
              <el-form-item prop="password">
                <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" placeholder="密码" show-password clearable></el-input>
              </el-form-item>
            </el-form>
          </div>
          <div>
            <el-button type="success" @click="login">登录</el-button>
          </div>
          <div>
            <el-tooltip effect="dark" content="请找综合服务中心-林永护">
              <el-button type="text">忘记密码?</el-button>
            </el-tooltip>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</div>
</template>

<style scoped>
.login {
  background-image: url("../assets/登录页背景.jpg");
  height: 97vh;
}
.login_card {
  width: 70%;
  height: 50%;
  position: relative;
  text-align: center;
  border-radius: 30px;
  left: 15%;
  top: 8vh;
  padding: 150px 0;
}
.login_card_img {
  background-image: url("../assets/登录页动图.jpg");
  width: 316px;
  height: 289px;
}
.login_card_left{
  float: left;
  position: relative;
  left: 100px;
}
.login_card_right {
  float: right;
  position: relative;
  left: -120px;
}
.login_card_input {
  margin-top: 30px;
}
.el-input {
  width: 300px;
}
/deep/ .el-input__inner {
  border-radius: 60px;
}
.el-button {
  width: 300px;
  border-radius: 60px;
  margin-top: 20px;
}
.login_card_title {

}
</style>
