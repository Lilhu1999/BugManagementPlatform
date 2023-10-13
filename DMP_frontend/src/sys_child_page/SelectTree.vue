<script>
export default {
  props:['multipleType',],
  data() {
    return {
      treeData:[],
      defaultProps: {
          children: 'children',
          label: 'name',
          pid:'id'
        },
      selectTree:[],
      value:[],
      id:[],
      multiple:false,
      showCheckbox:false,
    }
  },
  watch:{
    multipleType(newValue) {
      if (newValue===true) {
        this.multiple=true
        this.showCheckbox=true
      }
    },
  },
  mounted() {
    this.getTreeData()
    this.multiple = this.multipleType
    this.showCheckbox = this.multiple
  },
  methods: {
    // 点击节点回调事件
    handleNodeClick(data) {
      // 若未开启多选
      if (!this.multiple) {
        // 直接将value设置为当前点击的节点的name,id设置为当前点击节点的id
        this.value = data['name']
        this.id = data['id']
        //向父组件传递ID
        this.$emit('getPid',this.id)
      }else {
        console.log(data);
      }
    },
    // 执行set节点函数后，get当前选中的节点的节点数据
    checkedNodes(keys) {
      try{
        this.$refs.tree.setCheckedKeys(keys)
        this.$nextTick(()=>{
          console.log(this.$refs.tree.getCheckedKeys())
        })
      }catch (err) {
        console.log(err)
      }
    },
    // 获取当前被选中的节点
    getNodes(data, checkedNodes) {
      // 开启多选情况下，向父组件传递的是数组
      if (this.multiple) {
        const name_arr = []
        const id_arr = []
        console.log(data)
        console.log(checkedNodes)
        for (let key in checkedNodes.checkedNodes) {
          name_arr.push(checkedNodes.checkedNodes[key]['name'])
          id_arr.push(checkedNodes.checkedNodes[key]['id'])
        }
        this.value = name_arr
        this.id = id_arr
        this.$emit('getPid', this.id)
      }else {
        console.log(checkedNodes)
      }
    },
    // 获取树结构
    getTreeData() {
      this.$axios.get('api/getTree/',{
      }).then((response)=>{
        const res = response.data
        if (res['respCode']==='000000') {
          this.treeData = res['list']
        }else {
          console.log(res['respMsg'])
        }
      })
    },
  },
}
</script>

<template>
  <div>
    <el-select v-model="value" size="small" :multiple="multiple">
      <el-option :value="selectTree" class="opsty">
        <el-tree
          :data="treeData"
          :props="defaultProps"
          ref="tree"
          node-key="id"
          accordion
          :show-checkbox="showCheckbox"
          @node-click="handleNodeClick"
          @check="getNodes"
        >
        </el-tree>
      </el-option>
    </el-select>
  </div>
</template>

<style scoped>
.opsty {
  width: 100%;
  min-height: 200px;
  padding: 0 !important;
  margin: 0 ;
  overflow: auto;
}
</style>
