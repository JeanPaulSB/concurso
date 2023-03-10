<template>
  <div>
  <hello-world />
  <Participant name = "Andrés" city = "medellin" wrongQuestions = 4 />
  </div>
</template>

<script>
  import HelloWorld from '../components/HelloWorld'
  import Participant from '@/components/Participant.vue';

  export default {
    name: 'Home',

    components: {
      HelloWorld,
      Participant
    },
  }
</script>
