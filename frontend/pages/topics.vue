<template>
  <div>
    <div v-if="!erString.value" class="min-h-screen flex items-center justify-center">
      <div class="flex flex-wrap items-center justify-center">
        <div v-for="(topic, topicIndex) in topics" :key="topicIndex">
          <div
            class="w-64 border rounded-lg shadow-md cursor-pointer p-4 m-4"
            @click="toggleExpand(topic)"
          >
            <div class="text-lg font-semibold mb-2">{{ topic.name }}</div>

            <div v-if="isTopicExpanded(topic)" class="flex flex-wrap">
              <div v-for="(question, index) in topic.questions" :key="index">
                <nuxt-link
                  :to="`/questions/${question.id}`"
                  class="w-5 h-5 flex items-center justify-center m-1 rounded-full"
                  :class="question.attempted ? 'bg-green-500' : 'bg-red-500'"
                >
                  {{ index + 1 }}
                </nuxt-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h1>Please Log in</h1>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000';

const topics = ref([]);
const expandedTopics = ref([]);
const userString = ref(null);
userString.value = localStorage.getItem('user');
console.log(userString.value);
const error = ref('');

const user = JSON.parse(userString.value);

// Access the access token property from the user object
const token = user.access_token;

console.log(`Token : ${token}`);

async function getQuestions() {
  try {
    const response = await axios.get(`/api/questions/1`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    console.log(response.data[0]);
  } catch (e) {
    console.log(e);
  }
}



onMounted(() => {
  // This code will be executed when the component is mounted
  console.log('Component is mounted!');
  getQuestions();
});

topics.value = [
  {
    tid : 1,
    name: 'Topic 1',
    questions: [
      {
        id: 1,
        attempted: true
      },
      {
        id: 2,
        attempted: false
      }
    ]
  },
  {
    tid : 2,
    name: 'Topic 2',
    questions: [
      {
        id: 3,
        attempted: false
      },
      {
        id: 4,
        attempted: true
      }
    ]
  }
];

const toggleExpand = (topic) => {
  const index = expandedTopics.value.indexOf(topic);
  if (index === -1) {
    expandedTopics.value.push(topic);
  } else {
    expandedTopics.value.splice(index, 1);
  }
};

const isTopicExpanded = (topic) => expandedTopics.value.includes(topic);
</script>
