import axios from 'axios'

export function api(query) {
    return axios({
      method: 'post',
      url: '/graphql/',
      data: {
          'query': query
      }
    })
    .then((result) => {
      return result.data.data;
  });
}