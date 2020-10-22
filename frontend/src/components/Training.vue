<template>
  <div>
    <div>
      <codemirror>
        <span># write here</span>
      </codemirror>
    </div>
    <div>
      <button class="btn btn-success">Отправить</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Training',
  data () {
    return {
      'id': '',
      'text': '',
      'status': '',
      'created_at': ''
    }
  },
  methods: {
    createDecision () {
      this.$store.dispatch('createDecision', {
        id: this.id,
        text: this.text,
        status: this.status,
        created_at: this.created_at
      })
    }
  }
}

</script>

<style scoped>

</style>
