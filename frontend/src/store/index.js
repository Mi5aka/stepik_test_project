import Vuex from 'vuex'
import Vue from 'vue'
import {
  ADD_DECISION,
  CHECK_DECISION,
  SET_DECISIONS
} from './mutation-types'
import { Decision } from '../api/decisions'

Vue.use(Vuex)

// States
const state = {
  decisions: [] // list of decisions
}

const getters = {
  decisions: state => state.decisions // получаем список из состояния
}

// Mutations
const mutations = {
  // Add new decision at list
  [ADD_DECISION] (state, decision) {
    state.decisions = [decision, ...state.decisions]
  },
  // Убираем заметку из списка
  [CHECK_DECISION] (state, { id }) {
    state.decisions = state.decisions.filter(decision => {
      return decision.id !== id
    })
  },
  // Задаем список заметок
  [SET_DECISIONS] (state, { decisions }) {
    state.decisions = decisions
  }
}

const actions = {
  createDecision ({ commit }, decisionData) {
    Decision.create(decisionData).then(decision => {
      commit(ADD_DECISION, decision)
    })
  },
  checkDecision ({ commit }, decision) {
    Decision.retrieve(decision).then(response => {
      commit(CHECK_DECISION, decision)
    })
  },
  getDecisions ({ commit }) {
    Decision.list().then(decisions => {
      commit(SET_DECISIONS, { decisions })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
