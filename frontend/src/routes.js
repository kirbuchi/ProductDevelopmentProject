import RiskTypeForm from '@/components/RiskTypeForm';
import RiskTypeList from '@/components/RiskTypeList';

const routes = [
  { path: '/', name: 'home', component: RiskTypeList },
  { path: '/:id', name: 'form', component: RiskTypeForm },
];

export default routes;
