GetAllAccount();

let insertionType = "Insert";

$("#crudForm").on("submit", function (e) {
  e.preventDefault();
  let formData = new FormData();
  let methodType, URL_Link;

  formData.append("Name", $("#Name").val());
  formData.append("Email", $("#Email").val());
  formData.append("Phone", $("#Phone").val());
  formData.append("Username", $("#Username").val());
  formData.append("Password", $("#Password").val());

  if (insertionType == "Insert") {
    methodType = "POST";
    URL_Link = BASE_URL + "API/CRUD/with_noid";
  } else {
    methodType = "PUT";
    URL_Link = BASE_URL + "API/CRUD/with_id/" + $("#ID").val();
  }

  $.ajax({
    method: methodType,
    url: URL_Link,
    processData: false,
    contentType: false,
    data: formData,
    async: false,
    success: function (data) {
      if (!data.isError) {
        GetAllAccount();
        insertionType = "Insert";
        $("#crudForm").trigger("reset");
        $(".alert-success").removeClass("d-none");
        $(".alert-danger").addClass("d-none");
        $(".alert-success").text(data.Message);
      } else {
        $(".alert-success").addClass("d-none");
        $(".alert-danger").removeClass("d-none");
        $(".alert-danger").text(data.Message);
      }
    },
    error: function (data) {
      console.log(data);
    },
  });
});

$("#accountsTable tbody").on("click", ".delete", function () {
  const ID = $(this).attr("deleteID");

  if (confirm("Are you sure to delete")) {
    $.ajax({
      method: "DELETE",
      url: BASE_URL + "API/CRUD/with_id/" + ID,
      async: false,
      success: function (data) {
        $(".alert-success").removeClass("d-none");
        $(".alert-danger").addClass("d-none");
        $(".alert-success").text(data.Message);
        GetAllAccount();
      },
      error: function (data) {
        console.log(data);
      },
    });
  }
});

$("#accountsTable tbody").on("click", ".update", function () {
  const ID = $(this).attr("updateID");

  $.ajax({
    method: "GET",
    url: BASE_URL + "API/CRUD/with_id/" + ID,
    async: false,
    success: function (data) {
      insertionType = "Update";
      $("#Name").val(data.Message.Name);
      $("#Email").val(data.Message.Email);
      $("#Phone").val(data.Message.Phone);
      $("#Username").val(data.Message.Username);
      $("#Password").val(data.Message.Password);
      $("#ID").val(data.Message.id);
    },
    error: function (data) {
      console.log(data);
    },
  });
});

function GetAllAccount() {
  let DataMessage;

  $.ajax({
    method: "GET",
    url: BASE_URL + "API/CRUD/with_noid",
    async: false,
    success: function (data) {
      DataMessage = data.Message;
    },
    error: function (data) {
      console.log(data);
    },
  });

  let rows = "";
  if (DataMessage.length > 0) {
    for (let i = 0; i < DataMessage.length; i++) {
      rows +=
        `
      <tr>
        <td>` +
        DataMessage[i].Name +
        `</td>
        <td>` +
        DataMessage[i].Email +
        `</td>
        <td>` +
        DataMessage[i].Phone +
        `</td>
        <td>` +
        DataMessage[i].Username +
        `</td>
        <td>` +
        DataMessage[i].Password +
        `</td>
        <td>
          <Button class="btn btn-danger delete" deleteID = ` +
        DataMessage[i].id +
        `><i class="fas fa-trash-alt"></i></Button>
          <Button class="btn btn-primary update" updateID = ` +
        DataMessage[i].id +
        `><i class="fas fa-pencil"></i></Button>
        </td>
      </tr>
      `;
    }
  }

  $("#accountsTable tbody").html(rows);
}
