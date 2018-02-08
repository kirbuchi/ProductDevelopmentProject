import axios from 'axios';

const ENDPOINT_PATH = 'risk-types';
const FULL_API_URL = `${process.env.API_BASE_URL}/${ENDPOINT_PATH}`;

const loadRiskTypeSpecification = riskTypeId => (
  new Promise((resolve, reject) => {
    if (!riskTypeId) { reject('Invalid id'); }
    axios.get(`${FULL_API_URL}/${riskTypeId}`)
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
    axios.get(`${FULL_API_URL}`)
      .then((response) => { resolve(response.data); })
      .catch((err) => { reject(err); });
  })
);


export {
  loadRiskTypeSpecification,
  loadRiskTypeSpecificationList,
};
