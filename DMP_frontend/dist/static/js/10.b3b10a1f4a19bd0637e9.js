webpackJsonp([10],{cV6v:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s={components:{SelectTree:a("ynM2").a},data:function(){return{tableData:[],treeData:[],empSearchInput:"",options:[{value:0,label:"普通成员"},{value:1,label:"管理员"}],partDialogVisible:!1,empDialogVisible:!1,defaultProps:{children:"children",label:"name"},addEmpForm:{name:"",password:"",type:"",deptId:[]},addDeptForm:{name:"",id:[]}}},mounted:function(){this.getTreeData(),this.getEmp()},methods:{goBack:function(){window.history.back()},getPid:function(e){this.partDialogVisible?this.addDeptForm.id=e:this.empDialogVisible&&(this.addEmpForm.deptId=e)},getTreeData:function(){var e=this;this.$axios.post("api/getTree/",{params:{}}).then(function(t){var a=t.data;"000000"===a.respCode?e.treeData=a.list:e.$message.error(a.respMsg)})},addDept:function(){var e=this;this.$axios.post("api/dept/add/",{form:this.addDeptForm}).then(function(t){var a=t.data;"000000"===a.respCode?(e.$message.success("新增部门成功"),e.getTreeData()):e.$message.error(a.respMsg)})},addEmp:function(){var e=this;this.$axios.post("api/emp/add/",{form:this.addEmpForm}).then(function(t){var a=t.data;"000000"===a.respCode?e.$message.success("新增人员成功"):e.$message.error(a.respMsg)})},delEmp:function(e){var t=this;this.$axios.delete("api/emp/del/",{params:{id:e}}).then(function(a){var s=a.data;"000000"===s.respCode?(t.$message.success("删除成功"),t.getEmp(e)):t.$message.success(s.respMsg)})},getEmp:function(e){var t=this;this.$axios.get("api/emp/info/",{params:{id:e,name:this.empSearchInput}}).then(function(e){var a=e.data;"000000"===a.respCode?t.tableData=a.list:t.$message.error(a.respMsg)})},handleNodeClick:function(e,t){console.log("点击节点",e,t),this.getEmp(e.id)},clearDeptDialog:function(){this.addDeptForm.name="",this.addDeptForm.id=[]},clearEmpDialog:function(){this.addEmpForm.name="",this.addEmpForm.password="",this.addEmpForm.type="",this.addEmpForm.deptId=[]}}},l={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-card",[a("div",{attrs:{slot:"header"},slot:"header"},[a("el-page-header",{attrs:{content:"组织架构"},on:{back:e.goBack}})],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:6}},[a("el-card",{attrs:{shadow:"never"}},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("el-input",{staticStyle:{width:"150px"},attrs:{placeholder:"请输入部门名称",size:"small"}}),e._v(" "),a("el-button",{attrs:{size:"small",type:"primary"}},[e._v("查询")]),e._v(" "),a("el-button",{attrs:{size:"small",type:"success"},on:{click:function(t){e.partDialogVisible=!0}}},[e._v("新增")])],1),e._v(" "),a("div",[a("el-tree",{attrs:{data:e.treeData,props:e.defaultProps},on:{"node-click":e.handleNodeClick}})],1)])],1),e._v(" "),a("el-col",{attrs:{span:18}},[a("el-card",{attrs:{shadow:"never"}},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("el-input",{staticStyle:{width:"200px"},attrs:{placeholder:"请输入员工姓名",size:"small"},model:{value:e.empSearchInput,callback:function(t){e.empSearchInput=t},expression:"empSearchInput"}}),e._v(" "),a("el-button",{staticStyle:{float:"right"},attrs:{size:"small",type:"success"},on:{click:function(t){e.empDialogVisible=!0}}},[e._v("新增")])],1),e._v(" "),a("el-table",{attrs:{data:e.tableData,"max-height":"95vh",border:""}},[a("el-table-column",{attrs:{type:"index",label:"#",width:"50px",align:"center"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"人员姓名"}}),e._v(" "),a("el-table-column",{attrs:{prop:"type",label:"人员身份"},scopedSlots:e._u([{key:"default",fn:function(t){return[0===t.row.type?a("span",[e._v("普通用户")]):1===t.row.type?a("span",[e._v("管理员")]):e._e()]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"danger",size:"small"},on:{click:function(a){return e.delEmp(t.row.id)}}},[e._v("删除")])]}}])})],1)],1)],1)],1)],1),e._v(" "),a("el-dialog",{attrs:{visible:e.partDialogVisible,"destroy-on-close":""},on:{"update:visible":function(t){e.partDialogVisible=t},close:e.clearDeptDialog}},[a("el-form",{attrs:{inline:""}},[a("el-form-item",{attrs:{label:"部门名称"}},[a("el-input",{attrs:{size:"small"},model:{value:e.addDeptForm.name,callback:function(t){e.$set(e.addDeptForm,"name",t)},expression:"addDeptForm.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"所属部门"}},[a("SelectTree",{on:{getPid:e.getPid}})],1),e._v(" "),a("el-form-item",[a("div",{staticStyle:{float:"right"}},[a("el-button",{attrs:{type:"primary",size:"small"},on:{click:function(t){e.addDept(),e.partDialogVisible=!1}}},[e._v("\n            保存\n          ")]),e._v(" "),a("el-button",{attrs:{size:"small"},on:{click:function(t){e.partDialogVisible=!1}}},[e._v("\n            取消\n          ")])],1)])],1)],1),e._v(" "),a("el-dialog",{attrs:{visible:e.empDialogVisible,"destroy-on-close":""},on:{"update:visible":function(t){e.empDialogVisible=t},close:e.clearEmpDialog}},[a("el-form",{attrs:{inline:""}},[a("el-row",[a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"员工姓名"}},[a("el-input",{attrs:{size:"small"},model:{value:e.addEmpForm.name,callback:function(t){e.$set(e.addEmpForm,"name",t)},expression:"addEmpForm.name"}})],1)],1),e._v(" "),a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"人员密码"}},[a("el-input",{attrs:{size:"small","show-password":""},model:{value:e.addEmpForm.password,callback:function(t){e.$set(e.addEmpForm,"password",t)},expression:"addEmpForm.password"}})],1)],1),e._v(" "),a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"所属部门"}},[a("SelectTree",{on:{getPid:e.getPid}})],1)],1),e._v(" "),a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"人员身份"}},[a("el-select",{attrs:{size:"small"},model:{value:e.addEmpForm.type,callback:function(t){e.$set(e.addEmpForm,"type",t)},expression:"addEmpForm.type"}},e._l(e.options,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1)],1),e._v(" "),a("el-col",{attrs:{span:24}},[a("el-form-item",[a("div",[a("el-button",{attrs:{type:"primary",size:"small"},on:{click:function(t){e.addEmp(),e.empDialogVisible=!1}}},[e._v("\n                保存\n              ")]),e._v(" "),a("el-button",{attrs:{size:"small"},on:{click:function(t){e.empDialogVisible=!1}}},[e._v("\n                取消\n              ")])],1)])],1)],1)],1)],1)],1)},staticRenderFns:[]};var i=a("VU/8")(s,l,!1,function(e){a("rmu0")},"data-v-bf38d022",null);t.default=i.exports},rmu0:function(e,t){}});