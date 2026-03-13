<template>
  <div class="skills">
    <el-card>
      <template #header>
        <h2>🎯 技能清单</h2>
      </template>
      
      <el-collapse>
        <el-collapse-item v-for="(skills, category) in skillData" :key="category" :title="category">
          <el-table :data="skills" style="width: 100%">
            <el-table-column prop="skill" label="技能" />
            <el-table-column prop="count" label="次数" width="100">
              <template #default="{ row }">
                <div style="display: flex; align-items: center;">
                  <span style="margin-right: 10px;">{{ row.count }}</span>
                  <span>{{ '⭐'.repeat(Math.min(5, Math.ceil(row.count / 5))) }}</span>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const skillData = ref({
  '大数据': [
    { skill: 'Flink', count: 41 },
    { skill: 'Hudi', count: 35 },
    { skill: '大数据', count: 13 },
    { skill: 'Hive', count: 7 },
  ],
  '云计算': [
    { skill: 'OpenStack', count: 32 },
    { skill: 'CVM', count: 18 },
    { skill: 'K8s', count: 3 },
  ],
  '深度学习': [
    { skill: 'Transformer', count: 9 },
    { skill: 'PyTorch', count: 6 },
    { skill: '神经网络', count: 4 },
  ],
  '编程语言': [
    { skill: 'Java', count: 10 },
    { skill: 'Go', count: 9 },
    { skill: 'Python', count: 8 },
  ],
  'AI 芯片': [
    { skill: '昇腾', count: 5 },
    { skill: 'CANN', count: 4 },
  ],
})
</script>
