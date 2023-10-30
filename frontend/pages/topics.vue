<template>
    <div>
      <div class="min-h-screen flex items-center justify-center">
        <div class="flex flex-col items-center" style="margin-top: -30px;">
          <div v-for="(topic, topicIndex) in topics" :key="topicIndex">
            <div class="w-64 border rounded-lg shadow-md cursor-pointer p-4" @click="toggleExpand(topic)">
              <div class="text-lg font-semibold mb-2">{{ topic.name }}</div>
              
              <div v-if="isTopicExpanded(topic)" class="flex flex-wrap">
                <div v-for="(question, index) in topic.questions" :key="index">
                  <nuxt-link :to="`/questions/${question.id}`" class="w-5 h-5 flex items-center justify-center m-1 rounded-full" :class="question.attempted ? 'bg-green-500' : 'bg-red-500'">
                    {{ index + 1 }}
                  </nuxt-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>

<script setup>
const topics = ref([])
const expandedTopics = ref([])
topics.value = [
          {
            name: 'Topic 1',
            questions: [
              {
                id: 1,
                attempted: true,
              },
              {
                id: 2,
                attempted: false,
              },
            ],
          },
          {
            name: 'Topic 2',
            questions: [
              {
                id: 3,
                attempted: false,
              },
              {
                id: 4,
                attempted: true,
              },
            ],
          },
        ]
        function toggleExpand(topic) {
        const index = this.expandedTopics.indexOf(topic);
        if (index === -1) {
          this.expandedTopics.push(topic);
        } else {
          this.expandedTopics.splice(index, 1);
        }
      }
      function isTopicExpanded(topic) {
        return this.expandedTopics.includes(topic);
      }
</script>
  
 