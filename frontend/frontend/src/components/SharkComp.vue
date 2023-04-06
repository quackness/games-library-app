<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "SharkComp",
  data() {
    return {
      msg: "",
    };
  },
};
</script>
