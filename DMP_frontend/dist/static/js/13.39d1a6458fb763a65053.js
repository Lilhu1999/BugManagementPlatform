webpackJsonp([13],{T5L7:function(e,s){},y3ka:function(e,s,r){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var t={render:function(){var e=this,s=e.$createElement,r=e._self._c||s;return r("div",{staticClass:"login"},[r("div",[r("div",[r("el-card",{staticClass:"login_card"},[r("div",{staticClass:"login_card_left"},[r("div",{staticClass:"login_card_img"})]),e._v(" "),r("div",{staticClass:"login_card_right"},[r("div",{staticClass:"login_card_title"},[r("span",[e._v("测试管理平台demo用户登录")])]),e._v(" "),r("div",{staticClass:"login_card_input"},[r("el-form",{ref:"loginForm",attrs:{model:e.loginForm,rules:e.rules}},[r("el-form-item",{attrs:{prop:"username"}},[r("el-input",{attrs:{"prefix-icon":"el-icon-user",placeholder:"用户名",clearable:""},model:{value:e.loginForm.username,callback:function(s){e.$set(e.loginForm,"username",s)},expression:"loginForm.username"}})],1),e._v(" "),r("el-form-item",{attrs:{prop:"password"}},[r("el-input",{attrs:{"prefix-icon":"el-icon-lock",placeholder:"密码","show-password":"",clearable:""},model:{value:e.loginForm.password,callback:function(s){e.$set(e.loginForm,"password",s)},expression:"loginForm.password"}})],1)],1)],1),e._v(" "),r("div",[r("el-button",{attrs:{type:"success"},on:{click:e.login}},[e._v("登录")])],1),e._v(" "),r("div",[r("el-tooltip",{attrs:{effect:"dark",content:"请找综合服务中心-林永护"}},[r("el-button",{attrs:{type:"text"}},[e._v("忘记密码?")])],1)],1)])])],1)])])},staticRenderFns:[]};var o=r("VU/8")({data:function(){return{rules:{username:[{require:!0,message:"请输入用户名",tigger:"blur"}],password:[{require:!0,message:"请输入密码",tigger:"blur"}]},loginForm:{username:"",password:""}}},methods:{login:function(){var e=this;this.$axios.post("api/login/",{form:this.loginForm}).then(function(s){var r=s.data;"000000"===r.respCode?(e.$cookies.set("user_type",r.user_type,604800),e.$cookies.set("username",e.loginForm.username,604800),e.$router.push("/home"),e.$message.success("登录成功")):e.$message.error(r.respMsg)})}}},t,!1,function(e){r("T5L7")},"data-v-292a0534",null);s.default=o.exports}});