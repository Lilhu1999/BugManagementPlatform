webpackJsonp([10],{Kb2D:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a={data:function(){return{activePath:"",projectData:[{name:""}],searchInput:""}},mounted:function(){this.getProjectInfo(this.$route.query.id)},methods:{handleSelect:function(e,t){console.log(e,t)},saveActivePath:function(e){sessionStorage.setItem("pid",this.projectData[0].id),this.activePath=e},getProjectInfo:function(e){var t=this;this.$axios.get("api/project/info/",{params:{id:e}}).then(function(e){var n=e.data;"000000"===n.respCode?(t.projectData=n.list,console.log(t.projectData)):console.log(n.respMsg)})}}},i={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("el-container",[n("el-header",[n("el-menu",{staticClass:"el-menu-demo",attrs:{router:"","default-active":e.activePath,mode:"horizontal","active-text-color":"#409EFF"},on:{select:e.handleSelect}},[n("el-menu-item",{staticClass:"header-project-name"},[n("div",[n("el-icon",{staticClass:"el-icon-s-order"}),e._v(" "),n("span",[e._v(e._s(e.projectData[0].name))])],1)]),e._v(" "),n("el-menu-item",{attrs:{index:"/pj/requirement"},on:{click:function(t){return e.saveActivePath("/pj/requirement")}}},[e._v("需求")]),e._v(" "),n("el-menu-item",{attrs:{index:"/pj/defect"},on:{click:function(t){return e.saveActivePath("/pj/defect")}}},[e._v("缺陷")]),e._v(" "),n("el-menu-item",{attrs:{index:"/pj/testCase"},on:{click:function(t){return e.saveActivePath("/pj/testCase")}}},[e._v("测试用例")]),e._v(" "),n("el-menu-item",{attrs:{index:"/pj/document"},on:{click:function(t){return e.saveActivePath("/pj/document")}}},[e._v("文档")]),e._v(" "),n("el-menu-item",{attrs:{index:"/pj/iteration"},on:{click:function(t){return e.saveActivePath("/pj/iteration")}}},[e._v("迭代")]),e._v(" "),n("el-menu-item",{staticStyle:{float:"right"}},[n("el-input",{staticClass:"header_input",attrs:{"prefix-icon":"el-icon-search",size:"small"},model:{value:e.searchInput,callback:function(t){e.searchInput=t},expression:"searchInput"}})],1)],1)],1),e._v(" "),n("el-main",[n("router-view")],1)],1)],1)},staticRenderFns:[]};var c=n("VU/8")(a,i,!1,function(e){n("Rb/0")},"data-v-82ce2962",null);t.default=c.exports},"Rb/0":function(e,t){}});