import axios from 'axios';

// TODO: remove hardcoded url
const API_URL = 'http://127.0.0.1:5000/risk-types';


const loadRiskTypeSpecification = riskTypeId => (
  new Promise((resolve, reject) => {
    if (!riskTypeId) { reject('Invalid id'); }
    axios.get(`${API_URL}/${riskTypeId}`)
      .then((response) => {
        if (response.status !== 200) {
          return reject('Couldn\'t load request risk type.');
        }
        return resolve(response.data);
      }).catch((err) => { reject(err); });
  })
);


const loadRiskTypeSpecificationList = () => (
  new Promise((resolve, reject) => {
    axios.get(`${API_URL}`)
      .then((response) => { resolve(response.data); })
      .catch((err) => { reject(err); });
  })
);


export {
  loadRiskTypeSpecification,
  loadRiskTypeSpecificationList,
};
