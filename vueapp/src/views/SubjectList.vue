<template>
<div class="subject_list">
  <div v-for="subject in subjects" :key="subject.id">
    <p>{{ subject.title }}</p>
     <router-link :to="{name: 'subject_detail', params: { 'subject': subject.title }, query:{'subject': subject.title}}">Go to {{ subject.title }} questions</router-link>
  </div>
</div>
</template>

<script>
import getAPI from "@/axios-api";

export default {
       name: "SubjectList",
       data() {
            return {
                // tasks
                subjects: ['']
            }
        },
        methods: {
            async getData() {
                getAPI.get('/api/subject_list')
                  .then(response => {
                    this.subjects = response.data.subjects
                  })
              .catch(err => {
                console.log(err)
              })
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }

</script>

<style scoped>

</style>