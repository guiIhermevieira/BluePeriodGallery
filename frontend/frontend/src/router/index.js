import Vue from "vue";
import VueRouter from "vue-router";
import ArtGallery from "../components/ArtGallery.vue";
import SubmitNew from "../components/SubmitNew.vue";
import SubmissionsDetail from "../components/SubmissionsDetail.vue";
import LoginAdmin from "../components/LoginAdmin.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Arts",
    component: ArtGallery,
  },
  {
    path: "/submit",
    name: "Submit",
    component: SubmitNew,
  },
  {
    path: "/submissions",
    name: "Submissions",
    component: SubmissionsDetail,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginAdmin,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
