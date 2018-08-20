import axios from 'axios';

const API_URL = 'https://1uwlb89d1i.execute-api.eu-west-1.amazonaws.com/dev';

function callApi(path = '', method = 'get', payload = null) {
  return axios({
    method,
    url: API_URL + path,
    data: payload,
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.id_token}`,
    },
    crossDomain: true,
  });
}

/**
 * Add memo
 * @param {*} front
 * @param {*} back
 * @param lang
 * @param {*} tags
 * @param {*} notes
 */
export function addMemo(front, back, lang, tags = null, notes = null) {
  const payload = {
    front,
    back,
    lang,
    tags,
    notes,
  };
  return callApi('/addMemo', 'POST', payload);
}

/**
 * return a list of tags
 */
export function getTags() {
  return callApi('/tags');
}

/**
 * return info about connected user
 */
export function me() {
  return callApi('/me');
}

/**
 * return a list of memo
 */
export function getMemo() {
  return callApi('/list');
  /*
    .then(response => {
        this.info = response.data.bpi
    })
    .catch(error => {
        console.log(error)
        this.errored = true
    })
    .finally(() => this.loading = false)
    */
}
