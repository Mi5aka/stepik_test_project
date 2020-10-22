import { HTTP } from './common'

export const Decision = {
  create (config) {
    return HTTP.post('/decisions/', config).then(response => {
      return response.data
    })
  },
  retrieve (note) {
    return HTTP.get(`/decisions/${note.id}/`)
  },
  list () {
    return HTTP.get('/decisions/').then(response => {
      return response.data
    })
  }
}
