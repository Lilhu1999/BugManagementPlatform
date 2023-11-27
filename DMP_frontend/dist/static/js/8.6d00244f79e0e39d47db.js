webpackJsonp([8],{"0RM7":function(t,e){},LPJw:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var l={data:function(){return{uploadData:{pid:"",creator:""}}},mounted:function(){},methods:{onBeforeUpload:function(t){this.uploadData.pid=sessionStorage.getItem("pid"),this.uploadData.creator=this.$cookies.get("username");var e=t.size/1024/1024<10;return e||this.$message.error("文件大小不能超过10MB"),e}}},o={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("el-upload",{staticClass:"upload-demo",attrs:{accept:".doc,.docx,.xls,.xlsx,.txt,.pdf,.ppt,.pptx",data:this.uploadData,drag:"","show-file-list":!1,action:"api/upload/",multiple:"",limit:5,"before-upload":this.onBeforeUpload}},[e("i",{staticClass:"el-icon-upload"}),this._v(" "),e("div",{staticClass:"el-upload__text"},[this._v("将文件拖到此处，或"),e("em",[this._v("点击上传")])]),this._v(" "),e("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[this._v("只能上传doc/docx/xls/xlsx/txt/pdf/ppt/pptx文件，且文件大小不超过10MB")])])],1)},staticRenderFns:[]};var i={components:{Upload:a("VU/8")(l,o,!1,function(t){a("0RM7")},"data-v-04677cbe",null).exports},data:function(){return{dialogVisible:!1,tableData:[],searchForm:{fileName:"",creator:""}}},mounted:function(){this.getTableData()},methods:{getTableData:function(){var t=this;this.$axios.get("api/project/document/info/",{params:{pid:sessionStorage.getItem("pid"),fileName:this.searchForm.fileName,creator:this.searchForm.creator}}).then(function(e){var a=e.data;"000000"===a.respCode?t.tableData=a.list:t.$message.error(a.respMsg)})},download:function(t,e){this.$axios({method:"get",url:"api/download/",params:{uid:t},responseType:"blob"}).then(function(t){var a=t.data,l=window.URL.createObjectURL(new Blob([a])),o=document.createElement("a");o.href=l,o.setAttribute("download",e),document.body.appendChild(o),o.click()}).catch(function(t){console.log(t)})},delFile:function(t){var e=this;this.$confirm("确定删除该文件吗？",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){e.$axios.delete("api/project/document/del/",{params:{uid:t}}).then(function(t){var a=t.data;"000000"===a.respCode?(e.$message.success("删除成功"),e.getTableData()):e.$message.error(a.respMsg)})}).catch(function(){e.$message.info("取消删除")})}}},s={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",[a("el-form",{attrs:{inline:""}},[a("el-form-item",{attrs:{label:"文件名:"}},[a("el-input",{attrs:{size:"small",placeholder:"请输入文件名"},model:{value:t.searchForm.fileName,callback:function(e){t.$set(t.searchForm,"fileName",e)},expression:"searchForm.fileName"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"上传人:"}},[a("el-input",{attrs:{size:"small",placeholder:"请输入上传人"},model:{value:t.searchForm.creator,callback:function(e){t.$set(t.searchForm,"creator",e)},expression:"searchForm.creator"}})],1),t._v(" "),a("el-form-item",[a("el-button",{attrs:{size:"small",type:"primary"},on:{click:t.getTableData}},[t._v("查询")]),t._v(" "),a("el-button",{attrs:{size:"small",type:"warning"}},[t._v("重置")])],1)],1)],1),t._v(" "),a("div",[a("el-card",[a("div",{attrs:{slot:"header"},slot:"header"},[a("div",[a("el-button",{attrs:{size:"small",type:"success"},on:{click:function(e){t.dialogVisible=!0}}},[t._v("上传文档")]),t._v(" "),a("el-button",{attrs:{size:"small",type:"warning"}},[t._v("批量下载")])],1)]),t._v(" "),a("div",[a("el-table",{attrs:{data:t.tableData}},[a("el-table-column",{attrs:{type:"selection",width:"50"}}),t._v(" "),a("el-table-column",{attrs:{type:"index",label:"#",width:"50"}}),t._v(" "),a("el-table-column",{attrs:{label:"文件名",prop:"fileName"}}),t._v(" "),a("el-table-column",{attrs:{label:"上传人",prop:"creator"}}),t._v(" "),a("el-table-column",{attrs:{label:"上传时间",prop:"createTime"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作"},scopedSlots:t._u([{key:"default",fn:function(e){return a("div",{},[a("el-button",{attrs:{size:"small",type:"primary"},on:{click:function(a){return t.download(e.row.id,e.row.fileName)}}},[t._v("下载")]),t._v(" "),"管理员"===t.$cookies.get("user_type")?a("el-button",{attrs:{size:"small",type:"danger"},on:{click:function(a){return t.delFile(e.row.id)}}},[t._v("删除")]):t._e()],1)}}])})],1)],1)])],1),t._v(" "),a("div",[a("el-dialog",{attrs:{visible:t.dialogVisible,width:"400px"},on:{close:function(e){t.dialogVisible=!1,t.getTableData()}}},[a("div",{attrs:{slot:"title"},slot:"title"},[t._v("上传项目文档")]),t._v(" "),a("div",[a("Upload")],1)])],1)])},staticRenderFns:[]};var r=a("VU/8")(i,s,!1,function(t){a("lOkO")},"data-v-a711ceda",null);e.default=r.exports},lOkO:function(t,e){}});