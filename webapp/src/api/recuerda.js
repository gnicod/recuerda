import axios from 'axios';

const API_URL = 'https://ry0dldfiw5.execute-api.eu-west-1.amazonaws.com/dev';

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
 * @param {*} tag
 * @param {*} notes
 */
export function addMemo(front, back, tag = null, notes = null) {
  const payload = {
    front,
    back,
    tag,
    notes,
  };
  return callApi('/memo', 'POST', payload);
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
