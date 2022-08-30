import {createApp} from 'vue'
import App from "@/App";
import HomePage from "@/views/HomePage";
import SubjectList from "@/views/SubjectList";

import {createRouter, createWebHashHistory } from "vue-router";
import SubjectDetail from "@/views/SubjectDetail";
const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
      path: '/subjects/',
      name: 'subjects',
      component: SubjectList

    },
    {
      path: '/:subject/',
      name: 'subject_detail',
      component: SubjectDetail

    }
]
const router = new createRouter({
      history: createWebHashHistory(),
      routes
})
const app = createApp(App)
app.use(router)
app.mount('#app')