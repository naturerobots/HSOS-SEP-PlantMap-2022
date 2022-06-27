import axios from "axios";
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
