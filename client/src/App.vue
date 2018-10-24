<template>
  <div id="app">
    <Row>
      <Col span="16" push = '10'>
        <Upload action="/api/upload"
          name = 'myFile'
        >
          <Button icon="ios-cloud-upload-outline" id = 'upload'>Upload files</Button>
        </Upload>
      </Col>
    </Row>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
  /*#upload{*/
    /*width: 80px;*/
    /*height: 40px;*/
  /*}*/
</style>
