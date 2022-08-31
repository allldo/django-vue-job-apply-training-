<template>
<div class="list">
  <p>{{this.subject}}</p>
  <div class="questions_list" v-for="question in questions" :key="question.id">
    <span :id="question.id">{{ question.question }}
    </span>
    <span class="delete_question" v-on:click="delete_question">
      --  DELETE QUESTION</span>
  </div>
  <form action="" @submit.prevent="submitQuestion" method="post">
    <label>add question to this subject</label>
    <input id="question_input" name="question" placeholder="question">
    <button type="submit">submit</button>
  </form>
</div>
</template>

<script>
import getAPI from "@/axios-api";
import $ from 'jquery'

export default {
  name: "SubjectDetail",
 data() {
            return {
                // tasks
                subject: this.$route.params.subject,
              questions: []
            }
        },
        methods: {
            async getData() {
                getAPI.get(`/api/${this.$route.params.subject}`)
                  .then(response => {
                    console.log(response)
                    this.questions = response.data.questions
                  })
              .catch(err => {
                console.log(err)
              })
            },
            async submitQuestion(e){
              e.preventDefault();
              let qqe = e.target.question.value
              getAPI.post(
                  `/api/add_question/${this.subject}`,
                  {
                    question_data : qqe
                  }
              )
               .then(response => {
                 $('.list').append(
                     $('<div></div>').append(
                         $('<span></span>').text(response.data.new_question),
                         $('<span></span>').text('--  DELETE QUESTION').attr('v-on:click', 'delete_question'),
                 ).addClass('questions_list')
                 )
                 $('#question_input').val('')
                  })
              .catch(err => {
                console.log(err)
              })
            },
            async delete_question(e){
              let arr = $(e.target).siblings().attr('id')
              await getAPI.post(
                  `api/delete_question/${this.subject}/${arr}`
              ).then(response => {
                $('#'+response.data.item).parent().remove()
              })

            }
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }

}
</script>

<style scoped>

</style>