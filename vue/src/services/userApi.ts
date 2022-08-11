import axios from "axios";
import { userStore } from "@/stores/userStore";
import { storeToRefs } from "pinia";
import type { User, Token } from "@/types/user";

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
  firstName: string,
  lastName: string
): Promise<Token | undefined> {
  return await axios
    .post<Token>(baseURL + "/register", {
      username: username,
      password: password,
      first_name: firstName,
      last_name: lastName,
    })
    .then(function (response): Token {
      return response.data;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function logout(): Promise<boolean> {
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
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      //console.log(error.response);
      return false;
    });
}

export async function getUser(): Promise<User | undefined> {
  return await axios
    .get<User>(baseURL + "/user", {
      headers: {
        Authorization: "Token " + storeToRefs(userStore()).getToken.value.token,
      },
    })
    .then(function (response): User {
      return response.data;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function editUser(
  firstName?: string,
  lastName?: string,
  username?: string,
  password?: string
): Promise<boolean | undefined> {
  return await axios
    .put<boolean>(
      baseURL + "/user",
      {
        first_name: firstName,
        last_name: lastName,
        username: username,
        password: password,
      },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): undefined {
      //console.log(error.response);
      return undefined;
    });
}

export async function addPermissionToCompany(
  username: string,
  admin: boolean,
  companyId: number
): Promise<boolean> {
  return await axios
    .post(
      baseURL + "/companies/" + companyId + "/createPermission",
      {
        username: username,
        permission: admin ? "a" : "u",
      },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    });
}

export async function removePermissionFromCompany(
  username: string,
  companyId: number
): Promise<boolean | undefined> {
  return await axios
    .post(
      baseURL + "/companies/" + companyId + "/removePermission",
      {
        username: username,
      },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    });
}

export async function addPermissionToGarden(
  username: string,
  admin: boolean,
  companyId: number,
  gardenId: number
): Promise<boolean | undefined> {
  return await axios
    .post(
      baseURL +
        "/companies/" +
        companyId +
        "/gardens/" +
        gardenId +
        "/createPermission",
      {
        username: username,
        permission: admin ? "a" : "u",
      },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    });
}

export async function removePermissionFromGarden(
  username: string,
  companyId: number,
  gardenId: number
): Promise<boolean | undefined> {
  return await axios
    .post(
      baseURL +
        "/companies/" +
        companyId +
        "/gardens/" +
        gardenId +
        "/removePermission",
      {
        username: username,
      },
      {
        headers: {
          Authorization:
            "Token " + storeToRefs(userStore()).getToken.value.token,
        },
      }
    )
    .then(function (): boolean {
      return true;
    })
    .catch(function (): boolean {
      return false;
    });
}
