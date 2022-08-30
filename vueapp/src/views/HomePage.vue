<template>
    <div class="tasks_container">
        <div class="tasks_content">
            <h1>Tasks</h1>
            <ul class="tasks_list">
                <li v-for="subject in subjects" :key="subject.id">
                    <h2>{{ subject.title }}</h2>
                    <p>{{ subject.description }}</p>
                    <button @click="toggleTask(subject)">
                        {{ subject.completed ? 'Undo' : 'Complete' }}
                    </button>
                    <button @click="deleteTask(subject)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>

export default {
  name: "HomePage"
}

</script>

<style scoped>

</style>