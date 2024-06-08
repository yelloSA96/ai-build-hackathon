import useSWR,{mutate} from 'swr';
import { ChatDetails } from './utils';

const url = 'http://localhost:8000/api';


async function addRequest(data: ChatDetails) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

async function getRequest() {
    const response = await fetch(url);
    return response;
  }

export default function useOwnModelTrigger() {
    console.log("coming here")
  const { data, isValidating } = useSWR(url, getRequest);

  console.log("coming here2")


  const addRow = async (postData: ChatDetails) => {
    await addRequest(postData);
    mutate(url);
  };

  return {
    data: data ?? [],
    isValidating,
    addRow,
    
    
  };
}
