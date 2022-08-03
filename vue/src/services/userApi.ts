import axios from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { Token } from "@/types/user";

const baseURL = "http://127.0.0.1:8000";

export async function loginUser(
  username: string,
  password: string
): Promise<Token | undefined> {
  return await axios
    .post<Token>(baseURL + "/login", { username: username, password: password })
    .then(function (response): Token {
      return response.data;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function registerUser(
  username: string,
  password: string,
  firstname: string,
  lastname: string
): Promise<Token | undefined> {
  return await axios
    .post<Token>(baseURL + "/register", {
      username: username,
      password: password,
      first_name: firstname,
      last_name: lastname,
    })
    .then(function (response): Token {
      return response.data;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function logout(): Promise<void> {
  return await axios
    .post(
      baseURL + "/logout",
      {},
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): void {
      userStore().resetStore();
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}
