import Vue from "vue";
import VueRouter from "vue-router";
import SharkComp from "../components/SharkComp";
import GamesList from "../components/GamesList";
Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "SharkComp",
    component: SharkComp,
  },
  {
    path: "/games",
    name: "GamesList",
    component: GamesList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
