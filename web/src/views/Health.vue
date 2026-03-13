<template>
  <div class="health">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card>
          <template #header>
            <h3>📊 基础数据</h3>
          </template>
          <el-descriptions :column="1">
            <el-descriptions-item label="总书签">{{ health.total }}</el-descriptions-item>
            <el-descriptions-item label="唯一 URL">{{ health.unique_urls }}</el-descriptions-item>
            <el-descriptions-item label="重复收藏">{{ health.duplicates }}</el-descriptions-item>
          </el-descriptions>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card>
          <template #header>
            <h3>⭐ 内容质量</h3>
          </template>
          <el-progress :percentage="health.quality.high_quality_ratio" status="success" />
          <p>高质量：{{ health.quality.high_quality }}</p>
          <p>中质量：{{ health.quality.medium_quality }}</p>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card>
          <template #header>
            <h3>🌐 平台分布</h3>
          </template>
          <el-tag v-for="(count, platform) in health.platform_health.platforms" :key="platform" style="margin: 5px;">
            {{ platform }}: {{ count }}
          </el-tag>
          <p style="margin-top: 10px;">多样性：{{ health.platform_health.diversity }}</p>
        </el-card>
      </el-col>
    </el-row>

    <el-card style="margin-top: 20px;">
      <template #header>
        <h3>💡 综合建议</h3>
      </template>
      <el-alert
        v-for="(suggestion, index) in suggestions"
        :key="index"
        :title="suggestion"
        type="info"
        :closable="false"
        style="margin-bottom: 10px;"
      />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const health = ref({
  total: 328,
  unique_urls: 328,
  duplicates: 0,
  quality: {
    high_quality: 15,
    medium_quality: 299,
    high_quality_ratio: 4.6,
  },
  platform_health: {
    platforms: {
      'GitHub': 15,
      '知乎': 35,
      '技术博客': 97,
      '云厂商': 34,
    },
    diversity: '丰富',
  },
})

const suggestions = ref([
  '增加官方文档和高质量资源收藏',
  '保持学习节奏，持续积累',
  '拓展学习平台，增加多样性',
])
</script>
