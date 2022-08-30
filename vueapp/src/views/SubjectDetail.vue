<template>
<div>
  <p>{{this.subject}}</p>
</div>
</template>

<script>
import getAPI from "@/axios-api";

export default {
  name: "SubjectDetail",
 data() {
            return {
                // tasks
                subject: this.$route.params.subject
            }
        },
        methods: {
            async getData() {
                getAPI.get(`/api/${this.$route.params.subject}`)
                  .then(response => {
                    console.log(response)
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