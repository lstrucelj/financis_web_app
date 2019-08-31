<template>
  <div>
    <b-alert show dismissible fade variant="success">{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  props: ['message']
}
</script>
